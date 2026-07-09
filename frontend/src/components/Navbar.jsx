import { SearchCheck } from "lucide-react";

export default function Navbar() {
  return (
    <header className="bg-white shadow-sm border-b">

      <div className="max-w-7xl mx-auto px-6 py-4 flex items-center">

        <SearchCheck
          size={34}
          className="text-blue-600"
        />

        <span className="ml-3 font-bold text-2xl">
          AI SEO Audit Platform
        </span>

      </div>

    </header>
  );
}