import React from 'react';
import Router from './router/RouterConf'
import MuiThemeProvider from "material-ui/styles/MuiThemeProvider";
import AppBar from "material-ui/AppBar";

const App =()=>{
    return (
        <div>
          <MuiThemeProvider>
            <div>
              <AppBar
                  title="Login"
              />

        <Router/>

        </div>
  </MuiThemeProvider>
  </div>
  );

};

export default App;
