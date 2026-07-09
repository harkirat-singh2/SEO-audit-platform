import { Routes, Route } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import AuditDetails from "./pages/AuditDetails";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Dashboard />} />

      <Route
        path="/audits/:id"
        element={<AuditDetails />}
      />
    </Routes>
  );
}

export default App;