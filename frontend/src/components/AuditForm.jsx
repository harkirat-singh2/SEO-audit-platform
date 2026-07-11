import { useState } from "react";
import api from "../services/api";

export default function AuditForm({ onAuditCreated }) {
  const [url, setUrl] = useState("");
  const [maxPages, setMaxPages] = useState(5);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await api.post("/audits", {
        url,
        max_pages: maxPages,
      });

      // Fire callback to instantly update parent UI without a manual refresh
      if (onAuditCreated) {
        await onAuditCreated();
      }

      alert(`Audit Created!\nAudit ID: ${response.data.audit_id}`);
      setUrl("");
      setMaxPages(5);
    } catch (error) {
      console.error(error);
      alert("Audit failed.");
    }
    setLoading(false);
  }

  return (
    <form onSubmit={handleSubmit} className="bg-white shadow rounded-xl p-6 mt-8">
      <h2 className="text-2xl font-bold mb-6"> Run New Audit </h2>
      
      <div className="mb-5">
        <label className="block font-medium mb-2"> Website URL </label>
        <input
          type="url"
          required
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="https://example.com"
          className="w-full border rounded-lg px-4 py-3"
        />
      </div>
      
      <div className="mb-6">
        <label className="block font-medium mb-2"> Maximum Pages </label>
        <input
          type="number"
          min="1"
          max="100"
          value={maxPages}
          onChange={(e) => setMaxPages(Number(e.target.value))}
          className="w-32 border rounded-lg px-4 py-3"
        />
      </div>
      
      <button
        disabled={loading}
        className="flex items-center justify-center gap-2 bg-blue-600 hover:bg-blue-700 transition-colors duration-200 text-white font-semibold px-6 py-3 rounded-xl disabled:bg-gray-400 disabled:cursor-not-allowed"
      >
        {loading ? (
          <>
            {/* Tailwind animated SVG spinner */}
            <svg className="animate-spin h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
              <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
              <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
            </svg>
            <span>Running Audit...</span>
          </>
        ) : (
          "Run Audit"
        )}
      </button>
    </form>
  );
}
