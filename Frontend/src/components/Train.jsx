import React from 'react';
import {Typeahead} from 'react-bootstrap-typeahead';
import axios from 'axios';
import constants from './config/constants';


class Train extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        multiple: false,
        options: [],
        previousSourceStationCode: "NA",
        previousDestinationStationCode: "NA"
      };
      this.getTrainList = this.getTrainList.bind(this);
  }

  getTrainList(event) {
    if (this.state.previousSourceStationCode != this.props.sourceStationCode || this.state.previousDestinationStationCode != this.props.destinationStationCode) {
      axios.get(constants.train_list_endpoint,{params:{from:this.props.sourceStationCode, to:this.props.destinationStationCode}}).
      then((response) => {
          this.setState({options: response.data.train_list});
          this.setState({previousSourceStationCode: this.props.sourceStationCode });
          this.setState({previousDestinationStationCode: this.props.destinationStationCode });
      });
    }
  }

  render() {
    const multiple = this.state.multiple;
      return (
        <div>
          <Typeahead
            labelKey="name"
            multiple={multiple}
            options={this.state.options}
            placeholder={this.props.placeholderValue}
            onFocus={this.getTrainList}
            onChange={this.props.updateParentState}
          />
        </div>
      );
   }
}

export default Train;
