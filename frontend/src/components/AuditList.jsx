import AuditCard from "./AuditCard";
import EmptyState from "./EmptyState";

export default function AuditList({ audits }) {
  if (!audits || audits.length === 0) {
    return <EmptyState />;
  }

  return (
    <section className="mt-10">
      <h2 className="text-3xl font-bold mb-6">
        Recent Audits
      </h2>
      <div className="space-y-5">
        {audits.map((audit) => (
          <AuditCard key={audit.id} audit={audit} />
        ))}
      </div>
    </section>
  );
}
