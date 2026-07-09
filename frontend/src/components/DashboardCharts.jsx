import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
} from "recharts";

export default function DashboardCharts({ audits }) {
  const data = audits
    .filter(
      (audit) =>
        audit.pages &&
        audit.pages.length > 0 &&
        audit.pages[0].seo_analysis
    )
    .map((audit) => ({
      name: audit.website_url.replace("https://", "").replace("/", ""),
      score: audit.pages[0].seo_analysis.seo_score,
    }));

  return (
    <div className="bg-white rounded-2xl shadow-md p-6 mt-8">
      <h2 className="text-xl font-semibold mb-6">
        SEO Score by Website
      </h2>

      <ResponsiveContainer width="100%" height={320}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="name" />

          <YAxis domain={[0, 100]} />

          <Tooltip />

          <Bar
            dataKey="score"
            radius={[6, 6, 0, 0]}
          />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}