import React, { useContext, useState } from "react";
import { AuthContext } from "../context/AuthContext";
import { Link, useNavigate } from "react-router-dom";
import toast from "react-hot-toast";

function SignupPage() {
  const { signup } = useContext(AuthContext);
  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const navigate = useNavigate();

  const submit = async (e) => {
    e.preventDefault();
    setSubmitting(true);
    try {
      await signup(email, password, fullName);
      toast.success("Signup successful");
      navigate("/dashboard");
    } catch {
      toast.error("Signup failed. Email may already exist.");
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="page-wrapper no-header-page">
      <div className="container">
        <h2 className="title">Signup</h2>

        <form onSubmit={submit}>
          <label>Full Name</label>
          <input
            type="text"
            value={fullName}
            onChange={(e) => setFullName(e.target.value)}
            required
          />

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
            {submitting ? "Signing up..." : "Signup"}
          </button>
        </form>

        <p style={{ marginTop: 14, textAlign: "center" }}>
          Already have an account? <Link to="/login">Login</Link>
        </p>
      </div>
    </div>
  );
}

export default SignupPage;
