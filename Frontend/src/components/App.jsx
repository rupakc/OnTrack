import React from 'react'
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import { Button,Grid,Nav,NavItem,Navbar,NavDropdown,MenuItem,Form } from 'react-bootstrap'
import axios from 'axios'
import DateComponent from './DateComponent.jsx';
import Station from './Station.jsx';
import Train from './Train.jsx';
import Routemap from './Routemap.jsx';
import Home from './HomeComponent.jsx';
import Predict from './PredictComponent.jsx';
import Trigger from './CustomModal.jsx';


class App extends React.Component {
    render() {
    	return (
        <div>
        <Router>
          <div>
        <Navbar inverse>
            <Navbar.Header>
              <Navbar.Brand>
                <a href=".">OnTrack</a>
              </Navbar.Brand>
              <Navbar.Toggle />
                </Navbar.Header>
                <Navbar.Collapse>
            <Nav>
              <NavItem>
                <Link to={'/'}>Home</Link>
              </NavItem>
              <NavItem eventKey={2} href="#">
                <Link to={'/predict'}>Predict</Link>
              </NavItem>
            </Nav>
            <Nav pullRight>
              <NavItem> <Trigger label="About"/> </NavItem>
              <NavItem eventKey={2} href="https://git.corp.adobe.com/rupachak/OnTrack" target="_blank">
                Github
              </NavItem>
            </Nav>
        </Navbar.Collapse>
    </Navbar>
  <Switch>
     <Route exact path='/' component={Home} />
     <Route exact path='/predict' component={Predict} />
  </Switch>
</div>
</Router>
</div>
);
  }
}

export default App;
