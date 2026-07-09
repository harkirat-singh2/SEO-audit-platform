import StatsCard from "./StatsCard";
import {
  Globe,
  CheckCircle2,
  FileText,
  BarChart3,
} from "lucide-react";

export default function DashboardStats({ audits = [] }) {
  // 1. Calculate base audit metrics
  const total = audits.length;

  const completed = audits.filter(
    (audit) => audit.status?.toLowerCase() === "completed"
  ).length;

  // 2. Traversal variables for nested page metrics
  let pages = 0;
  let scoreSum = 0;
  let scoreCount = 0;

  // 3. Process nested metrics synchronously
  audits.forEach((audit) => {
    if (audit.pages) {
      pages += audit.pages.length;

      audit.pages.forEach((page) => {
        if (page.seo_analysis?.seo_score != null) {
          scoreSum += page.seo_analysis.seo_score;
          scoreCount++;
        }
      });
    }
  });

  const average = scoreCount === 0 ? 0 : Math.round(scoreSum / scoreCount);

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5 mb-8">
      <StatsCard
        title="Total Audits"
        value={total}
        icon={Globe}
        color="bg-blue-600"
      />

      <StatsCard
        title="Completed"
        value={completed}
        icon={CheckCircle2}
        color="bg-green-600"
      />

      <StatsCard
        title="Pages Crawled"
        value={pages}
        icon={FileText}
        color="bg-purple-600"
      />

      <StatsCard
        title="Average SEO Score"
        value={average}
        icon={BarChart3}
        color="bg-orange-500"
      />
    </div>
  );
}
