import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

// Optional: basic global styles
const rootStyle = {
  backgroundColor: "#f0f2f5",
  minHeight: "100vh",
};

const RootWrapper = () => (
  <div style={rootStyle}>
    <App />
  </div>
);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RootWrapper />
  </React.StrictMode>
);