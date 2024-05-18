import { List } from "@mui/material";
import TodoItem from "./TodoItem";

function TodoList({ todos, editTodo, deleteTodo, toggleTodo }) {
  return (
    <List>
      {todos.map((todo) => (
        <TodoItem
          key={todo.id}
          todo={todo}
          editTodo={editTodo}
          deleteTodo={deleteTodo}
          toggleTodo={toggleTodo}
        />
      ))}
    </List>
  );
}

export default TodoList;
