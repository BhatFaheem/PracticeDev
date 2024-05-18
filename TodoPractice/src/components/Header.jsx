import { AppBar, CssBaseline, Toolbar, Typography } from "@mui/material";
function Header() {
  return (
    <>
      <CssBaseline />
      <AppBar position="relative">
        <Toolbar style={{ justifyContent: "center" }}>
          <Typography variant="h3">Todo</Typography>
        </Toolbar>
      </AppBar>
    </>
  );
}

export default Header;
