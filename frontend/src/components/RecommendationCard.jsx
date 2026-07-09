export default function RecommendationCard({
  recommendation,
}) {
  const items = Object.values(recommendation).filter(
    (value) =>
      value &&
      value !== "No changes required."
  );

  return (
    <div className="bg-white rounded-xl shadow p-6 mt-6">
      <h2 className="text-lg font-semibold mb-4">
        AI Recommendations
      </h2>

      {items.length === 0 ? (
        <p>No recommendations.</p>
      ) : (
        <ul className="space-y-3 list-disc pl-5">
          {items.map((item, index) => (
            <li key={index}>
              {item}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}