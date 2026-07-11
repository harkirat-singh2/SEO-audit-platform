import AuditCard from "./AuditCard";
import EmptyState from "./EmptyState";

export default function AuditList({ audits, search, statusFilter, sortOrder }) {
  if (!audits || audits.length === 0) {
    return <EmptyState />;
  }

  // Filter audits by matching both search text and status dropdown selection
  const filteredAudits = audits.filter((audit) => {
    const matchesSearch = audit.website_url
      ?.toLowerCase()
      .includes(search.toLowerCase());

    const matchesStatus =
    statusFilter === "All" ||
    audit.status.trim().toLowerCase() ===
    statusFilter.trim().toLowerCase();

    return matchesSearch && matchesStatus;
  });

  // Display the empty state if the combined filters return no matches
  if (filteredAudits.length === 0) {
    return <EmptyState message="No audits found matching your criteria." />;
  }

  // Sort the filtered results chronologically based on the selection
  const sortedAudits = [...filteredAudits].sort((a, b) => {
    if (sortOrder === "Newest") {
      return new Date(b.started_at) - new Date(a.started_at);
    }
    return new Date(a.started_at) - new Date(b.started_at);
  });

  return (
    <section className="mt-10">
      <h2 className="text-3xl font-bold mb-6">
        Recent Audits
      </h2>
      <div className="space-y-5">
        {sortedAudits.map((audit) => (
          <AuditCard key={audit.id} audit={audit} />
        ))}
      </div>
    </section>
  );
}
