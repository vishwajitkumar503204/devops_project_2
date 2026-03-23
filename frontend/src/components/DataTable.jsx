import { useEffect, useState } from "react";
import { getData } from "../api";

export default function DataTable() {
  const [data, setData] = useState([]);

  const fetchData = () => {
    getData()
      .then((res) => setData(res.data))
      .catch((err) => console.error(err));
  };

  useEffect(() => {
    fetchData();

    const interval = setInterval(fetchData, 5000); // auto refresh
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ background: "#fff", padding: "20px", borderRadius: "10px" }}>
      <h3>Latest API Data</h3>
      <pre style={{ maxHeight: "400px", overflow: "auto" }}>
        {JSON.stringify(data, null, 2)}
      </pre>
    </div>
  );
}