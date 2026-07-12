import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import Navbar from "../components/Navbar";
import { getAudit } from "../services/api";
import ScoreCard from "../components/ScoreCard";
import MetricsTable from "../components/MetricsTable";
import RecommendationCard from "../components/RecommendationCard";
import DownloadButton from "../components/DownloadButton";

export default function AuditDetails() {
  const { id } = useParams();

  const [audit, setAudit] = useState(null);
  const [loading, setLoading] = useState(true);

  // Fix: Added 'id' to the dependency array to refetch if the URL changes
  useEffect(() => {
    fetchAudit();
  }, [id]);

  async function fetchAudit() {
    try {
      const response = await getAudit(id);
      setAudit(response.data);
    } catch (error) {
      console.error(error);
    }
    setLoading(false);
  }

  if (loading) {
    return (
      <>
        <Navbar />
        <main className="max-w-7xl mx-auto p-6">
          <div className="text-slate-500 animate-pulse font-medium">
            Loading...
          </div>
        </main>
      </>
    );
  }

  return (
    <>
      <Navbar />

      <main className="max-w-7xl mx-auto p-6">
        <div className="space-y-8">
          {/* Header Title */}
          <div>
            <h1 className="text-3xl font-bold text-slate-900 tracking-tight">
              Audit Details
            </h1>
            <p className="text-slate-500 mt-1">
              {audit?.website_url}
            </p>
          </div>

          {/* Main Layout Grid */}
          <div className="grid lg:grid-cols-3 gap-6">
            {/* Score Card Section */}
            <div className="lg:col-span-1">
              <ScoreCard
                score={audit?.pages?.[0]?.seo_analysis?.seo_score ?? 0}
              />
            </div>

            {/* Metrics & Recommendations Content Area */}
            <div className="lg:col-span-2 space-y-6">
              <MetricsTable seo={audit?.pages?.[0]?.seo_analysis} />

              <RecommendationCard
                recommendation={audit?.pages?.[0]?.recommendation}
              />
            </div>
          </div>

          {/* Full-width Actions / Download Button Section */}
          <div className="border-t border-slate-100 pt-2">
            {/* Fallback to URL 'id' if 'audit.id' hasn't populated yet */}
            <DownloadButton auditId={audit?.id || id} />
          </div>
        </div>
      </main>
    </>
  );
}
