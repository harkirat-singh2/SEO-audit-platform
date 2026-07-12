export default function RecommendationCard({ recommendation }) {
  // 1. Early return for null, undefined, or empty objects
  if (!recommendation || (typeof recommendation === "object" && Object.keys(recommendation).length === 0)) {
    return <EmptyCardMessage />;
  }

  // 2. Extract entries and filter out "no changes required" using case-insensitive checks
  const items = Object.entries(recommendation ?? {}).filter(
    ([_, value]) =>
      value &&
      value.trim().toLowerCase() !== "no changes required" &&
      value.trim().toLowerCase() !== "no changes required."
  );

  return (
    <div className="bg-white rounded-xl shadow p-6 mt-6">
      <h2 className="text-lg font-semibold mb-4 text-gray-800">
        AI Recommendations
      </h2>

      {items.length === 0 ? (
        <p className="text-gray-500">No recommendations.</p>
      ) : (
        <ul className="space-y-4">
          {items.map(([key, value]) => (
            <li key={key} className="flex gap-2 text-gray-700">
              <span className="font-semibold text-gray-900 whitespace-nowrap">
                {key
                  .replaceAll("_", " ")
                  .replace(/\b\w/g, c => c.toUpperCase())}:
              </span>
              <span>{value}</span>
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
