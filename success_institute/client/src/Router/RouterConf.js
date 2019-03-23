import React from 'react';
import {BrowserRouter as Router, Route} from 'react-router-dom'
import Login from '../components/Login'
function Routes (){
    return(
        <Router>
            <Route exact path='/' component={Login}/>
            <Route path='*'></Route>
        </Router>
    );
};

export default Routes;