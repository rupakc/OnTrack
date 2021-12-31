import React from 'react'
import ReactDOM from 'react-dom'

import 'react-bootstrap-typeahead/css/Typeahead.css';
import 'bootstrap/dist/css/bootstrap.css'

import App from './components/App'
import DateComponent from './components/DateComponent.jsx'
import Train from './components/Train.jsx'
import Station from './components/Station.jsx'
import Routemap from './components/Routemap.jsx';


ReactDOM.render(<App textVal="Submit"/>, document.getElementById('app'))
