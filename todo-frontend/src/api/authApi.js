import client from "./client";

export const loginApi = async ({ email, password }) => {
  const res = await client.post("/auth/login", { email, password });
  return res.data; // contains access_token
};

export const signupApi = async ({ email, password, fullName }) => {
  const res = await client.post("/auth/signup", {
    email,
    password,
    full_name: fullName,
  });
  return res.data;
};

export const meApi = async () => {
  const res = await client.get("/users/me");
  return res.data; // { id, email, full_name, ... }
};
