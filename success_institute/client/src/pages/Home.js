import React from "react";
import { Typography, Button } from "@material-ui/core/";
import axios from "../services/axios";

const Home = () => {
  let studenst = [];
  return (
    <div>
      <Typography variant="display1" align="center" gutterBottom>
        Hello World
      </Typography>
      <ul>
        {studenst.map(student => (
          <li id={student.id}>student.name</li>
        ))}
      </ul>
      <Button
        onClick={() => {
          axios
            .get("students")
            .then(data => {
              studenst = data;
            })
            .catch(err => {
              console.log({ err });
            });
        }}
      >
        Clickme
      </Button>
    </div>
  );
};

export default Home;
