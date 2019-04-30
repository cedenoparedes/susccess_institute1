import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import Login from "../components/Login";
import Home from "../pages/Home";

const RoutesList = [
  { path: "/login", component: Login },
  { path: "/home", component: Home }
];

const Routersetter = route => {
  return (
    <Route
      path={route.path}
      render={props => (
        // pass the sub-routes down to keep nesting
        <route.component {...props} routes={route.routes} />
      )}
    />
  );
};

function Routes() {
  return (
    <Router>
      {RoutesList.map((route, key) => (
        <Routersetter key={key} {...route} />
      ))}
    </Router>
  );
}

export default Routes;
