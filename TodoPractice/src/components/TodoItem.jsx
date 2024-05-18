import { IconButton, ListItem, TextField, Checkbox } from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import EditIcon from "@mui/icons-material/Edit";
import SaveIcon from "@mui/icons-material/Save";
import React, { useState } from "react";

function TodoItem({ todo, editTodo, deleteTodo, toggleTodo }) {
  const [edit, setEdit] = useState(false);
  const [editText, setEditText] = useState(todo.text);

  const handleEditText = (e) => {
    console.log(e.target.value);
    setEditText(e.target.value);
  };
  const handleSubmitEditText = (e) => {
    e.preventDefault();
    if (editText.length > 0) {
      editTodo(todo.id, editText);
      setEdit(false);
      setEditText("");
    }
  };
  return (
    <>
      <ListItem>
        <Checkbox
          checked={todo.isCompleted}
          onChange={() => toggleTodo(todo.id)}
        />
        {edit ? (
          <>
            <TextField
              value={editText}
              fullWidth
              onChange={handleEditText}
              variant="outlined"
            />
            <IconButton
              variant="contained"
              color="primary"
              type="submit"
              onClick={handleSubmitEditText}
            >
              <SaveIcon />
            </IconButton>
          </>
        ) : (
          <>
            <TextField
              variant="outlined"
              value={todo.text}
              fullWidth
              disabled={todo.isComplete ? true : false}
            />
            <IconButton onClick={() => setEdit(true)}>
              <EditIcon />
            </IconButton>
            <IconButton onClick={() => deleteTodo(todo.id)}>
              <DeleteIcon />
            </IconButton>
          </>
        )}
      </ListItem>
    </>
  );
}

export default TodoItem;
