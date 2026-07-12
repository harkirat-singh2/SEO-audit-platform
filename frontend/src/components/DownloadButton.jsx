import { Download } from "lucide-react";

export default function DownloadButton({ auditId }) {
  function downloadReport() {
    const apiUrl = import.meta.env.VITE_API_URL;
    const url = `${apiUrl}/audits/${auditId}/report`;
    console.log("Opening:", url);
    
    // Instead of opening, redirect the current tab
    window.location.href = url;
  }

  return (
    <button
      onClick={downloadReport}
      className="mt-6 flex items-center gap-2 bg-blue-600 hover:bg-blue-700 transition-colors duration-200 text-white font-semibold px-6 py-3 rounded-xl"
    >
      <Download size={18} />
      Download PDF Report
    </button>
  );
}
