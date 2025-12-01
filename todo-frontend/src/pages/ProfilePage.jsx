import React, { useContext } from "react";
import Header from "../components/Header";
import { AuthContext } from "../context/AuthContext";
import toast from "react-hot-toast";

function ProfilePage() {
  const { user, logout } = useContext(AuthContext);

  const handleLogout = () => {
    if (!window.confirm("Are you sure you want to logout?")) return;
    logout();
    toast.success("Logged out");
  };

  return (
    <>
      <Header />
      <div className="page-wrapper">
        <div className="container">
          <h2 className="title">Profile</h2>
          <p>
            <b>Name:</b> {user?.full_name || user?.fullName || "-"}
          </p>
          <p>
            <b>Email:</b> {user?.email}
          </p>
          <button
            onClick={handleLogout}
            style={{ background: "#dc2626", marginTop: 20 }}
          >
            Logout
          </button>
        </div>
      </div>
    </>
  );
}

export default ProfilePage;
