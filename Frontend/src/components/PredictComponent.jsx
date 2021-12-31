import React from 'react'
import { Button,Grid,Nav,NavItem,Navbar,NavDropdown,MenuItem,Form } from 'react-bootstrap'
import axios from 'axios'
import DateComponent from './DateComponent.jsx';
import Station from './Station.jsx';
import Train from './Train.jsx';
import Routemap from './Routemap.jsx';
import Loader from './CustomLoader.jsx';
import constants from './config/constants';


class Predict extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      source: 'HWH',
      destination: 'NDLS',
      trainNum: 12274,
      trainDate: new Date().toISOString().slice(0,10),
      data: '',
      url: '',
      showResults: false,
      showLoader: false
    };
    this.clickHandler = this.clickHandler.bind(this);
    this.updateStateSource = this.updateStateSource.bind(this);
    this.updateStateDestination = this.updateStateDestination.bind(this);
    this.updateStateTrainNum = this.updateStateTrainNum.bind(this);
    this.updateStateDate = this.updateStateDate.bind(this);
  }

    clickHandler() {
      this.setState({showLoader: true});
      axios.get(constants.delay_explaination_endpoint,{params:{train_num: this.state.trainNum, from: this.state.source, to: this.state.destination, date: this.state.trainDate}}).
      then((response) => {
        this.setState({url: response.data.filepath});
        this.setState({showResults: true});
        this.setState({showLoader: false});
        this.forceUpdate();
      });
    }

    updateStateSource(e) {
      this.setState({source: e[0].code});
    }

    updateStateDestination(e) {
      this.setState({destination: e[0].code});
      this.forceUpdate();
    }

    updateStateTrainNum(e) {
      this.setState({trainNum: e[0].number});
    }

    updateStateDate(outputDate) {
      this.setState({trainDate: outputDate});
      this.forceUpdate();
    }

  render() {
    return (
      <div>
        {this.state.showLoader ? <Loader/> : null}
        <Grid bsClass='container'>
              <DateComponent updateParentState={this.updateStateDate}/> <br/>
              <Station placeholderValue='Choose Source Station' updateParentState={this.updateStateSource} /> <br/>
              <Station placeholderValue='Choose Destination Station' updateParentState={this.updateStateDestination} /> <br/>
              <Train placeholderValue='Choose A Train' sourceStationCode={this.state.source}
              destinationStationCode={this.state.destination} updateParentState={this.updateStateTrainNum}/> <br/>
          <div className='text-center'>
            <Button bsStyle="success"  onClick={this.clickHandler}>Submit</Button>
          </div> <br/>
          { this.state.showResults ? <Routemap url={this.state.url} /> : null }
        </Grid>
      </div>
    );
  }
}

export default Predict
