import axios from "axios";
let token = "";
const httpapi = axios.create({
  withCredentials: true,
  headers: {
    Accept: "application/json",
    "Content-type": "application/json",
    Authorization: `Token ${token}`
  }
});

httpapi.interceptors.response.use(response => (response, error) => {
  if (error.response.status === 401 || error.response.status === 504) {
    console.log({ response, error });
  } else {
    console.log({ response, error });
  }
});
export default () => httpapi;
