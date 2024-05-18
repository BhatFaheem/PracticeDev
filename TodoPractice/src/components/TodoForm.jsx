import { Button, Grid, TextField } from "@mui/material";
import React, { useState } from "react";

function TodoForm({ addTodo }) {
  const [todo, setTodo] = useState("");

  const handleChange = (e) => {
    setTodo(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (todo.length > 0) {
      addTodo(todo);
      setTodo("");
    }
  };
  return (
    <>
      <Grid container m={2} alignItems={"center"} justifyContent={"center"}>
        <Grid item xs={8} mr={5}>
          <TextField
            label="Add Todo"
            fullWidth
            variant="outlined"
            value={todo}
            onChange={handleChange}
          />
        </Grid>
        <Grid>
          <Button
            type="submit"
            variant="contained"
            size="large"
            onClick={handleSubmit}
          >
            Add
          </Button>
        </Grid>
      </Grid>
    </>
  );
}

export default TodoForm;
