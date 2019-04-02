import {createStore, applyMiddleware} from 'redux'
import thunk from 'redux-thunk'
import rootReducers from ''
let initialState={};
let middleware =[thunk];

const store = createStore(
  rootReducers,
  initialState,
  applyMiddleware(...middleware)
);

export default store;
