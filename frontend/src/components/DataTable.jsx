import { useEffect, useState } from "react";
import { getData } from "../api";

export default function DataTable() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchData = () => {
    setLoading(true);
    setError(null);
    
    getData()
      .then((res) => {
        setData(res.data);
        setLoading(false);      })
      .catch((err) => {
        console.error(err);
        setError(err.message);
        setLoading(false);
      });
  };

  useEffect(() => {
    fetchData();

    const interval = setInterval(fetchData, 5000); // auto refresh every 5s
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={containerStyle}>
      <div style={headerStyle}>
        <h3>📊 Latest API Data</h3>
        <button onClick={fetchData} style={buttonStyle} disabled={loading}>
          {loading ? "⏳ Loading..." : "🔄 Refresh"}
        </button>
      </div>

      {error && (
        <div style={errorStyle}>
          ❌ Error: {error}
        </div>
      )}

      {loading && !data.length ? (
        <div style={loadingStyle}>Loading data...</div>
      ) : (
        <>
          <div style={statsStyle}>
            <span>Total Records: <strong>{data.length}</strong></span>
            <span>Last Updated: <strong>{new Date().toLocaleTimeString()}</strong></span>
          </div>
          <pre style={preStyle}>
            {JSON.stringify(data, null, 2)}
          </pre>
        </>
      )}
    </div>
  );
}

const containerStyle = {
  background: "#fff",
  padding: "20px",
  borderRadius: "10px",
  boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
};

const headerStyle = {
  display: "flex",
  justifyContent: "space-between",
  alignItems: "center",
  marginBottom: "15px",
};

const buttonStyle = {
  padding: "8px 16px",
  background: "#007bff",
  color: "#fff",
  border: "none",
  borderRadius: "5px",
  cursor: "pointer",
  fontSize: "14px",
};

const errorStyle = {
  background: "#ffebee",
  color: "#c62828",
  padding: "10px",
  borderRadius: "5px",
  marginBottom: "15px",
};

const loadingStyle = {
  textAlign: "center",
  padding: "20px",
  color: "#666",
};

const statsStyle = {
  display: "flex",
  justifyContent: "space-between",
  padding: "10px",
  background: "#f8f9fa",
  borderRadius: "5px",
  marginBottom: "15px",
  fontSize: "14px",
};

const preStyle = {
  maxHeight: "400px",
  overflow: "auto",
  background: "#f8f9fa",
  padding: "15px",
  borderRadius: "5px",
  fontSize: "13px",
  lineHeight: "1.5",
};