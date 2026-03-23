import axios from "axios";

// ✅ FIX: Use relative URL so it goes through Nginx proxy
const API = axios.create({
  baseURL: "/api", // No longer need the full URL
  timeout: 10000,
  headers: {
    "Content-Type": "application/json",
  },
});

// Request interceptor for logging
API.interceptors.request.use(
  (config) => {
    console.log(`📤 Request: ${config.method.toUpperCase()} ${config.url}`);
    return config;
  },
  (error) => {
    console.error("❌ Request Error:", error);
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
API.interceptors.response.use(
  (response) => {
    console.log(`✅ Response: ${response.status} ${response.config.url}`);
    return response;
  },
  (error) => {
    if (error.response) {
      // Server responded with error status
      console.error("❌ Response Error:", error.response.status, error.response.data);
    } else if (error.request) {
      // Request made but no response
      console.error("❌ No Response:", error.request);
    } else {
      // Something else happened
      console.error("❌ Error:", error.message);
    }
    return Promise.reject(error);
  }
);

export const getData = () => API.get("/data");
export const getHealth = () => API.get("/health");

export default API;