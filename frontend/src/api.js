import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8080", // later change to ALB URL
});

export const getData = () => API.get("/data");
export const getHealth = () => API.get("/health");