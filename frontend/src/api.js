import axios from "axios";

const API = axios.create({
  baseURL: import.meta.env.VITE_API_URL,// later change to ALB URL
});

export const getData = () => API.get("/data");
export const getHealth = () => API.get("/health");