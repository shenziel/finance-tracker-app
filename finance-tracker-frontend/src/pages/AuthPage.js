import React from "react";
import Login from "../components/Login";
import Register from "../components/Register";
import "../App.css";

const AuthPage = () => {
  return (
    <div className="main">
      <h1>Finance Tracker App</h1>
      <input type="checkbox" id="chk" aria-hidden="true" />
      <Login />
      <Register />
    </div>
  );
};

export default AuthPage;
