export default function RecommendationCard({ recommendation }) {
  // 1. Early return for null, undefined, or empty objects
  if (!recommendation || (typeof recommendation === "object" && Object.keys(recommendation).length === 0)) {
    return <EmptyCardMessage />;
  }

  // 2. Extract entries, sanitize values, and filter out negative responses safely
  const recommendations = Object.entries(recommendation)
    .map(([key, value]) => [key, String(value ?? '').trim()])
    .filter(([_, val]) => val && !val.toLowerCase().startsWith("no changes required"));

  return (
    <div className="bg-white rounded-xl shadow p-6 mt-6">
      <h2 className="text-lg font-semibold mb-4 text-gray-800">
        AI Recommendations
      </h2>

      {recommendations.length === 0 ? (
        <p className="text-gray-500">No recommendations.</p>
      ) : (
        <ul className="space-y-4">
          {recommendations.map(([key, value]) => (
            <li key={key} className="text-gray-700">
              <strong className="text-sm font-semibold text-gray-900 block mb-1">
                {key
                  .replaceAll("_", " ")
                  .replace(/\b\w/g, (c) => c.toUpperCase())}
              </strong>
              <p className="leading-relaxed">{value}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

// Fallback visual component for empty states
function EmptyCardMessage() {
  return (
    <div className="bg-white rounded-xl shadow p-6 mt-6">
      <h2 className="text-lg font-semibold mb-4 text-gray-800">
        AI Recommendations
      </h2>
      <p className="text-gray-500">
        No AI recommendations available.
      </p>
    </div>
  );
}
