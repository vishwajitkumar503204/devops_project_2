import StatusCard from "./components/StatusCard";
import DataTable from "./components/DataTable";

function App() {
  return (
    <div style={container}>
      <h1>📊 DevOps API Dashboard</h1>
      <StatusCard />
      <DataTable />
    </div>
  );
}

const container = {
  maxWidth: "900px",
  margin: "auto",
  padding: "20px",
  fontFamily: "Arial",
};

export default App;