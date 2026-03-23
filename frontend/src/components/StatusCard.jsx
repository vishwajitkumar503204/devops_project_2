import { useEffect, useState } from "react";
import { getHealth } from "../api";

export default function StatusCard() {
  const [status, setStatus] = useState("Checking...");
  const [details, setDetails] = useState(null);

  const checkHealth = () => {
    getHealth()
      .then((res) => {
        setStatus("🟢 Healthy");
        setDetails(res.data);
      })
      .catch((err) => {
        setStatus("🔴 Down");
        setDetails({ error: err.message });
      });
  };

  useEffect(() => {
    checkHealth();
    
    // Check health every 30 seconds
    const interval = setInterval(checkHealth, 30000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={cardStyle}>
      <h3>Service Status</h3>
      <p style={{ fontSize: "24px", margin: "10px 0" }}>{status}</p>
      {details && (
        <pre style={{ fontSize: "12px", background: "#fff", padding: "10px", borderRadius: "5px" }}>
          {JSON.stringify(details, null, 2)}
        </pre>
      )}
    </div>
  );
}

const cardStyle = {
  padding: "20px",
  borderRadius: "10px",
  background: "#f4f4f4",
  marginBottom: "20px",
  boxShadow: "0 2px 4px rgba(0,0,0,0.1)",
};