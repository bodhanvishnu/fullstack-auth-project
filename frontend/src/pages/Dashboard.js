import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../api/axios";
import "../styles/dashboard.css";

function Dashboard() {
  const navigate = useNavigate();

  const [profile, setProfile] = useState(null);
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const token = localStorage.getItem("access_token");
    if (!token) {
      navigate("/login");
    }
  }, [navigate]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const profileRes = await API.get("/user/profile");
        setProfile(profileRes.data);

        const role = profileRes.data["user role"];

        if (role && role.toUpperCase() === "ADMIN") {
          const usersRes = await API.get("/admin/get-all-users");
          setUsers(usersRes.data["user list"]);
        }
      } catch (error) {
        localStorage.clear();
        navigate("/login");
      }
    };

    fetchData();
  }, [navigate]);

  const handleLogout = () => {
    localStorage.clear();
    navigate("/login");
  };

  if (!profile) {
    return <p>Loading...</p>;
  }

  return (
    <div className="page">
      <div className="dashboard-container">
        <h1>Dashboard</h1>

        <div className="card">
          <h2>My Profile</h2>
          <p><b>Username:</b> {profile.username}</p>
          <p><b>Role:</b> {profile["user role"]}</p>
        </div>

        {profile["user role"] &&
          profile["user role"].toUpperCase() === "ADMIN" && (
            <div className="card">
              <h2>All Users</h2>

              <table>
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Username</th>
                    <th>Role</th>
                  </tr>
                </thead>
                <tbody>
                  {users.map((user) => (
                    <tr key={user.id}>
                      <td>{user.id}</td>
                      <td>{user.username}</td>
                      <td>{user.role}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}

        <button className="logout-btn" onClick={handleLogout}>
          Logout
        </button>
      </div>
    </div>
  );
}

export default Dashboard;
