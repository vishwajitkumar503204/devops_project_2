import { useEffect, useState } from "react";
import { getHealth } from "../api";

export default function StatusCard() {
  const [status, setStatus] = useState("Checking...");

  useEffect(() => {
    getHealth()
      .then(() => setStatus("🟢 Healthy"))
      .catch(() => setStatus("🔴 Down"));
  }, []);

  return (
    <div style={cardStyle}>
      <h3>Service Status</h3>
      <p>{status}</p>
    </div>
  );
}

const cardStyle = {
  padding: "20px",
  borderRadius: "10px",
  background: "#f4f4f4",
  marginBottom: "20px",
};