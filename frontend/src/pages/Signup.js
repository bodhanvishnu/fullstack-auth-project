import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../api/axios";
import "../styles/auth.css";

function Signup() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (password !== confirmPassword) {
      alert("Passwords do not match");
      return;
    }

    try {
      await API.post("/auth/signup", {
        username,
        password,
        confirm_password: confirmPassword,
      });

      navigate("/login");
    } catch (error) {
      alert("Signup failed");
    }
  };

  return (
    <div className="page">
      <div className="card">
        <h1>Signup</h1>

        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />

          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <input
            type="password"
            placeholder="Confirm Password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
          />

          <button className="auth-button" type="submit">Signup</button>
        </form>
        <p className="auth-link">
        Already have an account?{" "}
        <span onClick={() => navigate("/login")}>Login</span>
      </p>
      </div>
    </div>
  );
}

export default Signup;
