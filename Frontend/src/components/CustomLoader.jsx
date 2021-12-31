import React from 'react';
import './css/loader.css';

class Loader extends React.Component {
  render() {
    return(
      <div id="divLoading" style={{'background-color': '#00000087'}} className="img-responsive center-block">
      </div>
    );
  }
}

export default Loader
