import React, { useContext, useState } from "react";
import { AuthContext } from "../context/AuthContext";
import { Link, useNavigate } from "react-router-dom";
import toast from "react-hot-toast";

function LoginPage() {
  const { login } = useContext(AuthContext);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const navigate = useNavigate();

  const submit = async (e) => {
    e.preventDefault();
    setSubmitting(true);
    try {
      await login(email, password);
      toast.success("Logged in successfully");
      navigate("/dashboard");
    } catch {
      toast.error("Invalid email or password");
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="page-wrapper no-header-page">
      <div className="container">
        <h2 className="title">Login</h2>

        <form onSubmit={submit}>
          <label>Email</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />

          <label>Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />

          <button type="submit" disabled={submitting}>
            {submitting ? "Logging in..." : "Login"}
          </button>
        </form>

        <p style={{ marginTop: 14, textAlign: "center" }}>
          Don't have an account? <Link to="/signup">Signup</Link>
        </p>
      </div>
    </div>
  );
}

export default LoginPage;
