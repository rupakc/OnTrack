import React from "react";
import './css/home.css';
import './css/predictstyle.css';

class Routemap extends React.Component {
  render() {
    return (
      <div className="text-center" style={{overflow:'auto'}}>
        <iframe id="homeMap" src={this.props.url} />
      </div>
    );
  }
}

export default Routemap
