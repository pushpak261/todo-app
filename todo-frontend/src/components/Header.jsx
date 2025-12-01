import { Link } from "react-router-dom";

const Header = () => (
  <div className="top-header">
    <Link to="/dashboard">Dashboard</Link>
    <Link to="/profile">Profile</Link>
  </div>
);

export default Header;
