export default function StatsCard({
  title,
  value,
  icon: Icon,
  color,
}) {
  return (
    <div
      className="
        bg-white
        rounded-2xl
        shadow-md
        hover:shadow-xl
        transition-all
        duration-300
        p-6
        border
      "
    >
      <div className="flex justify-between items-center">

        <div>

          <p className="text-gray-500 text-sm">
            {title}
          </p>

          <h2 className="text-4xl font-bold mt-3">
            {value}
          </h2>

        </div>

        <div
          className={`${color} p-4 rounded-xl text-white`}
        >
          <Icon size={28} />
        </div>

      </div>
    </div>
  );
}