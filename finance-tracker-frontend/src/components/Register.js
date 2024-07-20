// src/components/Register.js

import React, { useState } from "react";
import axios from "axios";

const Register = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async () => {
    try {
      const response = await axios.post(
        "http://localhost:5000/users/register",
        {
          username,
          password,
        }
      );
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="signup">
      <form onSubmit={handleRegister}>
        <label className="loginLabel" htmlFor="chk" aria-hidden="true">
          Register
        </label>
        <input
          className="loginInput"
          type="text"
          name="txt"
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
          id="password"
          value={password}
        />
        <button className="loginButton" type="submit">
          Sign up
        </button>
      </form>
    </div>
  );
};

export default Register;
