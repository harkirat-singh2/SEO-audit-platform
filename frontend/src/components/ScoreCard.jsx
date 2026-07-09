export default function ScoreCard({ score }) {
  function getColor() {
    if (score >= 80) return "text-green-600";
    if (score >= 50) return "text-yellow-600";
    return "text-red-600";
  }

  return (
    <div className="bg-white rounded-xl shadow p-6">
      <h2 className="text-lg font-semibold mb-4">
        SEO Score
      </h2>

      <p className={`text-5xl font-bold ${getColor()}`}>
        {score}
      </p>

      <p className="text-gray-500 mt-2">
        out of 100
      </p>
    </div>
  );
}