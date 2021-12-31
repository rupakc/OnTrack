import React from 'react'
import { Button,Grid,Nav,NavItem,Navbar,NavDropdown,MenuItem,Form } from 'react-bootstrap'
import axios from 'axios'
import Station from './Station.jsx';
import Train from './Train.jsx';
import Routemap from './Routemap.jsx';
import Loader from './CustomLoader.jsx';
import constants from './config/constants';


class Home extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      source: 'HWH',
      destination: 'NDLS',
      trainNum: 12274,
      data: '',
      url: '',
      showResults: false,
      showLoader: false
    };

    this.clickHandler = this.clickHandler.bind(this);
    this.updateStateSource = this.updateStateSource.bind(this);
    this.updateStateDestination = this.updateStateDestination.bind(this);
    this.updateStateTrainNum = this.updateStateTrainNum.bind(this);
  }

    clickHandler() {
      this.setState({showLoader: true});
      axios.get(constants.routemap_endpoint,{params:{train_num: this.state.trainNum}}).
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

  render() {
    return (
      <div>
        {this.state.showLoader ? <Loader/> : null}
        <Grid bsClass='container'>
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

export default Home
