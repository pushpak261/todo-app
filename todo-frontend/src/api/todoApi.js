import client from "./client";

export const getTodosApi = async () => {
  const res = await client.get("/todos/");
  return res.data;
};

export const createTodoApi = async (title) => {
  const res = await client.post("/todos/", { title });
  return res.data;
};

export const updateTodoApi = async (id, data) => {
  const res = await client.patch(`/todos/${id}`, data);
  return res.data;
};


export const deleteTodoApi = async (id) => {
  const res = await client.delete(`/todos/${id}`);
  return res.data;
};
