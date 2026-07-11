import { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import AuditForm from "../components/AuditForm";
import DashboardStats from "../components/DashboardStats";
import DashboardCharts from "../components/DashboardCharts";
import AuditList from "../components/AuditList";
import api from "../services/api";
import LoadingSpinner from "../components/LoadingSpinner";
import ErrorMessage from "../components/ErrorMessage";
import Hero from "../components/Hero";
import AuditToolbar from "../components/AuditToolbar"; 

export default function Dashboard() {
  const [audits, setAudits] = useState([]);
  const [search, setSearch] = useState("");
  const [statusFilter, setStatusFilter] = useState("All");
  const [sortOrder, setSortOrder] = useState("Newest");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchAudits();
  }, []);

  async function fetchAudits() {
    try {
      setLoading(true);
      const response = await api.get("/audits/");
      setAudits(response.data);
    } catch {
      setError("Unable to load audits.");
    } finally {
      setLoading(false);
    }
  }

  if (loading) {
    return <LoadingSpinner />;
  }

  if (error) {
    return <ErrorMessage message={error} />;
  }

  return (
    <>
      <Navbar />
      <main className="max-w-7xl mx-auto p-6">
        <div className="space-y-8">
          <Hero />
          <AuditToolbar
            search={search}
            setSearch={setSearch}
            statusFilter={statusFilter}
            setStatusFilter={setStatusFilter}
            sortOrder={sortOrder}
            setSortOrder={setSortOrder}
          />
          <DashboardStats audits={audits} />
          <DashboardCharts audits={audits} />
          <AuditForm onAuditCreated={fetchAudits} />
          <AuditList 
            audits={audits} 
            search={search} 
            statusFilter={statusFilter} 
            sortOrder={sortOrder}
          />
        </div>
      </main>
    </>
  );
}
