export default function MetricsTable({ seo }) {
  const metrics = [
    ["Title Length", seo.title_length],
    ["Meta Description Length", seo.meta_description_length],
    ["Word Count", seo.word_count],
    ["H1 Count", seo.h1_count],
    ["H2 Count", seo.h2_count],
    ["Images", seo.total_images],
    ["Images Without Alt", seo.images_without_alt],
    ["Internal Links", seo.internal_links],
    ["External Links", seo.external_links],
    ["Language", seo.language],
    ["Canonical", seo.has_canonical ? "Yes" : "No"],
  ];

  return (
    <div className="bg-white rounded-xl shadow p-6 mt-6">
      <h2 className="text-lg font-semibold mb-4">
        SEO Metrics
      </h2>

      <table className="w-full border-collapse">
        <tbody>
          {metrics.map(([label, value]) => (
            <tr
              key={label}
              className="border-b"
            >
              <td className="py-3 font-medium">
                {label}
              </td>

              <td className="py-3 text-right">
                {String(value)}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}