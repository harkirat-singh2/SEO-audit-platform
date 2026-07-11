import { Link } from "react-router-dom";
import {
  Globe,
  CalendarDays,
  ArrowRight,
  CheckCircle2,
  Clock3,
  XCircle,
} from "lucide-react";

export default function AuditCard({ audit }) {
  function getStatusIcon() {
    switch (audit.status?.toLowerCase()) {
      case "completed":
        return <CheckCircle2 className="text-green-600" size={18} />;

      case "running":
        return <Clock3 className="text-yellow-500" size={18} />;

      default:
        return <XCircle className="text-red-500" size={18} />;
    }
  }

  function getStatusColor() {
    switch (audit.status?.toLowerCase()) {
      case "completed":
        return "bg-green-100 text-green-700";

      case "running":
        return "bg-yellow-100 text-yellow-700";

      default:
        return "bg-red-100 text-red-700";
    }
  }

  // Format the audit initialization timestamp
  const formattedDate = new Date(audit.started_at + "Z").toLocaleString(
  "en-IN",
  {
    dateStyle: "medium",
    timeStyle: "short",
    timeZone: "Asia/Kolkata",
  }
);

  return (
    <div
      className="
      bg-white
      rounded-2xl
      border
      shadow-sm
      hover:shadow-lg
      hover:-translate-y-1
      transition-all
      duration-300
      p-6
      "
    >
      <div className="flex justify-between items-start">
        <div>
          <div className="flex items-center gap-3">
            <Globe className="text-blue-600" size={22} />
            <h2 className="font-bold text-xl">
              {audit.website_url}
            </h2>
          </div>

          <div className="mt-5 flex items-center gap-2">
            {getStatusIcon()}
            <span
              className={`
                px-3
                py-1
                rounded-full
                text-sm
                font-medium
                ${getStatusColor()}
              `}
            >
              {audit.status}
            </span>
          </div>

          <div className="flex items-center gap-2 mt-5 text-gray-500">
            <CalendarDays size={18} />
            <span>{formattedDate}</span>
          </div>
        </div>

        <Link
          to={`/audits/${audit.id}`}
          className="
          flex
          items-center
          gap-2
          text-blue-600
          hover:text-blue-800
          font-semibold
          "
        >
          View Details
          <ArrowRight size={18} />
        </Link>
      </div>
    </div>
  );
}
