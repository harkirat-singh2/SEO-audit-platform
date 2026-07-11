export default function AuditToolbar({
  search,
  setSearch,
  statusFilter,
  setStatusFilter,
}) {
  return (
    <div className="flex flex-col md:flex-row gap-4 items-center justify-between">

      <input
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        placeholder="Search websites..."
        className="
          flex-1
          border
          rounded-xl
          px-4
          py-3
        "
      />

      <select
        value={statusFilter}
        onChange={(e) => setStatusFilter(e.target.value)}
        className="
          w-full
          md:w-52
          border
          rounded-xl
          px-4
          py-3
        "
      >
        <option>All</option>
        <option>Completed</option>
        <option>Running</option>
        <option>Failed</option>
      </select>

    </div>
  );
}