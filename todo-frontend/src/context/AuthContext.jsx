import React, { createContext, useEffect, useState } from "react";
import { loginApi, signupApi, meApi } from "../api/authApi";

export const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // load user on refresh
  useEffect(() => {
    const init = async () => {
      const token = localStorage.getItem("access_token");
      if (token) {
        try {
          const me = await meApi();
          setUser(me);
        } catch {
          localStorage.removeItem("access_token");
        }
      }
      setLoading(false);
    };
    init();
  }, []);

  const login = async (email, password) => {
    const res = await loginApi({ email, password });
    localStorage.setItem("access_token", res.access_token);
    const me = await meApi();
    setUser(me);
  };

  const signup = async (email, password, fullName) => {
    await signupApi({ email, password, fullName });
    await login(email, password);
  };

  const logout = () => {
    localStorage.removeItem("access_token");
    setUser(null);
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        loading,
        isAuthenticated: !!user,
        login,
        signup,
        logout,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};
