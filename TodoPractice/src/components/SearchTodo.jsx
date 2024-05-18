import {
  TextField,
  Grid,
  Button,
  Paper,
  List,
  ListItem,
  ListItemText,
} from "@mui/material";
import { React, useState } from "react";

function SearchTodo({ todos }) {
  const [searchText, setSearchText] = useState("");
  const [suggestions, setSuggestions] = useState([]);
  const [isFocus, setIsFocus] = useState(false);
  const handleChange = (e) => {
    const val = e.target.value;
    setSearchText(val);
    const matchingTodos = todos.filter((todo) =>
      todo.text.toLowerCase().includes(val.toLowerCase())
    );
    setSuggestions(matchingTodos);
  };
  const handleFocus = () => {
    setIsFocus(true);
  };

  const handleBlur = () => {
    setIsFocus(false);
  };
  return (
    <>
      <Grid container m={2} alignItems={"center"} justifyContent={"center"}>
        <Grid item xs={5} mr={5}>
          <TextField
            label="Search Todo"
            fullWidth
            variant="outlined"
            value={searchText}
            onChange={handleChange}
            onFocus={handleFocus}
            onBlur={handleBlur}
          />
        </Grid>
        <Grid>
          <Button type="submit" variant="contained" size="large">
            Search
          </Button>
        </Grid>
      </Grid>
      {isFocus && suggestions.length > 0 && (
        <Paper elevation={6} style={{ maxHeight: 200, overflowY: "auto" }}>
          <List>
            {suggestions.map((todo) => (
              <ListItem key={todo.id}>
                <ListItemText primary={todo.text} />
              </ListItem>
            ))}
          </List>
        </Paper>
      )}
    </>
  );
}

export default SearchTodo;
