import React from "react";
import Router from "./router/RouterConf";
import Store from "./context";
import MuiThemeProvider from "material-ui/styles/MuiThemeProvider";
import { AppBar } from "material-ui";

const App = () => (
  <Store>
    <MuiThemeProvider>
      <div>
        <AppBar title="Login" />
        <Router />
      </div>
    </MuiThemeProvider>
  </Store>
);

export default App;
