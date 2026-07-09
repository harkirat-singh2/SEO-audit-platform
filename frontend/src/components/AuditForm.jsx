import { useState } from "react";
import api from "../services/api";

export default function AuditForm() {
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

      alert(
        `Audit Created!\nAudit ID: ${response.data.audit_id}`
      );

      setUrl("");
      setMaxPages(5);

    } catch (error) {
      console.error(error);

      alert("Audit failed.");
    }

    setLoading(false);
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white shadow rounded-xl p-6 mt-8"
    >
      <h2 className="text-2xl font-bold mb-6">
        Run New Audit
      </h2>

      <div className="mb-5">
        <label className="block font-medium mb-2">
          Website URL
        </label>

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
        <label className="block font-medium mb-2">
          Maximum Pages
        </label>

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
        className="
bg-blue-600
hover:bg-blue-700
transition-colors
duration-200
text-white
font-semibold
px-6
py-3
rounded-xl
disabled:bg-gray-400
disabled:cursor-not-allowed
"
      >
        {loading ? "Running Audit..." : "Run Audit"}
      </button>
    </form>
  );
}