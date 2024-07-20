const useAuth = () => {
  // Replace this logic with your actual authentication check
  const isAuthenticated = () => {
    return !!localStorage.getItem("authToken"); // Check if token exists in local storage
  };

  return { isAuthenticated };
};

export default useAuth;
