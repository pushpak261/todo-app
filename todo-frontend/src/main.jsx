import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import { AuthProvider } from "./context/AuthContext";
import { BrowserRouter } from "react-router-dom";
import { Toaster } from "react-hot-toast";
import "./style.css"; // <--- make sure file name matches

ReactDOM.createRoot(document.getElementById("root")).render(
  <AuthProvider>
    <BrowserRouter>
      <App />
      <Toaster position="top-center" />
    </BrowserRouter>
  </AuthProvider>
);
