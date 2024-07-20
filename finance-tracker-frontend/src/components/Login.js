import React, { useState } from "react";
import { loginUser } from "../services/api";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const navigate = useNavigate(); // Use useNavigate for redirecting

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await loginUser(username, password);
      const token = response.data.token; // Adjust this based on your API response

      console.log(token);
      console.log(username);
      console.log(password);

      if (token) {
        localStorage.setItem("authToken", token); // Save token to local storage
        navigate("/"); // Redirect to home page or other protected route
      }
    } catch (error) {
      setMessage(
        "Login failed: " + error.response?.data?.message || error.message
      );
    }
  };

  return (
    <div className="login">
      <form onSubmit={handleLogin}>
        <label className="loginLabel" htmlFor="chk" aria-hidden="true">
          Login
        </label>
        {message && <p style={{ color: "red" }}>{message}</p>}
        <input
          className="loginInput"
          type="text"
          placeholder="User name"
          onChange={(e) => setUsername(e.target.value)}
          value={username}
        />
        <input
          className="loginInput"
          type="password"
          placeholder="Password"
          required
          onChange={(e) => setPassword(e.target.value)}
        />
        <button className="loginButton" type="submit">
          Login
        </button>
      </form>
    </div>
  );
};

export default Login;
