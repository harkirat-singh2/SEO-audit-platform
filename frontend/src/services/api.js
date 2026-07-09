import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const getAudits = () => api.get("/audits/");

export const getAudit = (id) =>
  api.get(`/audits/${id}`);

export default api;