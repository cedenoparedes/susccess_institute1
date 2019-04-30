import React, { useState } from "react";
import axios from "axios";

export const myContext = React.createContext({});

const Store = ({ children }) => {
  const [user, setUser] = useState({ username: "", password: "" });

  const login = usr => {
    return new Promise(async (resolve, reject) => {
      try {
        let response = await axios.post("login", usr);
        resolve(response.data);
      } catch (error) {
        console.log({ error });
        reject(error);
      }
    });
  };
  return (
    <myContext.Provider value={{ user, setUser, login }}>
      {children}
    </myContext.Provider>
  );
};

export default Store;
