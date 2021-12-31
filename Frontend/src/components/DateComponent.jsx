import React, { Component } from "react";
import DateTimeField from "react-bootstrap-datetimepicker";
import './css/datepicker.css';

class DateComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      date: new Date(),
      format: "YYYY-MM-DD",
      inputFormat: "DD/MM/YYYY",
      mode: "date"
    };
  }

  handleChange = (newDate) => {
    return this.setState({date: newDate});
  }

  render() {
    const {date, format, mode, inputFormat} = this.state;
    return (<DateTimeField
      dateTime={date}
      format={format}
      inputFormat={inputFormat}
      onChange={this.props.updateParentState}
      viewMode={mode}
    />);
  }
}

module.exports = DateComponent;
