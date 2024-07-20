// src/services/api.js

import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:5000",
});

export const loginUser = (username, password) => {
  return API.post("/users/login", { username, password });
};

export const registerUser = (username, password) => {
  return API.post("/users/register", { username, password });
};

// Similarly, you can create functions for login, addTransaction, getTransactions, getSummary, etc.
