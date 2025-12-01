import React, { useEffect, useState } from "react";
import Header from "../components/Header";
import {
  getTodosApi,
  createTodoApi,
  updateTodoApi,
  deleteTodoApi,
} from "../api/todoApi";
import toast from "react-hot-toast";

function DashboardPage() {
  const [todos, setTodos] = useState([]);
  const [title, setTitle] = useState("");
  const [loading, setLoading] = useState(true);
  const [btnLoading, setBtnLoading] = useState(false);

  const loadTodos = async () => {
    try {
      setLoading(true);
      const data = await getTodosApi();
      setTodos(data);
    } catch (err) {
      console.error(err);
      toast.error("Failed to load todos");
    } finally {
      setLoading(false);
    }
  };

  const handleAddTodo = async (e) => {
    e.preventDefault();
    if (!title.trim()) {
      toast.error("Enter a todo!");
      return;
    }
    try {
      setBtnLoading(true);
      await createTodoApi(title.trim());
      setTitle("");
      toast.success("Todo added");
      await loadTodos();
    } catch (err) {
      console.error(err);
      toast.error("Failed to add todo");
    } finally {
      setBtnLoading(false);
    }
  };

  const toggleTodo = async (todo) => {
    try {
      await updateTodoApi(todo.id, { completed: !todo.completed });
      toast.success(todo.completed ? "Marked incomplete" : "Marked complete");
      await loadTodos();
    } catch (err) {
      console.error(err);
      toast.error("Failed to update");
    }
  };

  const handleDelete = async (todo) => {
    if (!window.confirm("Delete this task?")) return;
    try {
      await deleteTodoApi(todo.id);
      toast.success("Todo deleted");
      await loadTodos();
    } catch (err) {
      console.error(err);
      toast.error("Failed to delete");
    }
  };

  useEffect(() => {
    loadTodos();
  }, []);

  return (
    <>
      <Header />
      <div className="page-wrapper">
        <div className="container">
          <h2 className="title">My Todos</h2>

          <form onSubmit={handleAddTodo}>
            <input
              type="text"
              placeholder="Add new task..."
              value={title}
              onChange={(e) => setTitle(e.target.value)}
            />
            <button type="submit" disabled={btnLoading}>
              {btnLoading ? "Adding..." : "Add"}
            </button>
          </form>

          {loading ? (
            <p className="text-center" style={{ marginTop: 20 }}>
              Loading...
            </p>
          ) : (
            <div style={{ marginTop: 20 }}>
              {todos.length === 0 && (
                <p className="text-center">No todos yet. Add one!</p>
              )}

              {todos.map((todo) => (
                <div key={todo.id} className="todo-row">
                  <div className="todo-left">
                    <input
                      type="checkbox"
                      checked={todo.completed}
                      onChange={() => toggleTodo(todo)}
                    />
                    <span
                      className={
                        todo.completed ? "completed-text" : "normal-text"
                      }
                    >
                      {todo.title}
                    </span>
                  </div>

                  <button className="delete-btn" onClick={() => handleDelete(todo)}>
                    Delete
                  </button>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </>
  );
}

export default DashboardPage;
