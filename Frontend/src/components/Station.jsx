import React from 'react';
import {Typeahead} from 'react-bootstrap-typeahead';
import axios from 'axios';
import constants from './config/constants';

class Station extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      multiple: false,
      options: []
    };
}

  componentDidMount() {
    axios.get(constants.station_list_endpoint).then((response) => {
          this.setState({options : response.data.station_list});
      });
  }

  render() {
    const multiple = this.state.multiple;
      return (
          <Typeahead
            labelKey="name"
            multiple={multiple}
            options={this.state.options}
            placeholder={this.props.placeholderValue}
            onChange = {this.props.updateParentState}
          />
      );
  }
}

export default Station;
