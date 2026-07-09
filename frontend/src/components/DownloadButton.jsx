import { Download } from "lucide-react";

export default function DownloadButton({ auditId }) {
  function downloadReport() {
    window.open(
      `http://127.0.0.1:8000/audits/${auditId}/report`,
      "_blank"
    );
  }

  return (
    <button
      onClick={downloadReport}
      className="
        mt-6
        flex
        items-center
        gap-2
        bg-blue-600
        hover:bg-blue-700
        transition-colors
        duration-200
        text-white
        font-semibold
        px-6
        py-3
        rounded-xl
      "
    >
      <Download size={18} />
      Download PDF Report
    </button>
  );
}
