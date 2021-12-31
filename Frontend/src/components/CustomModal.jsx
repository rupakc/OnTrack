import React from 'react';
import {Button, Modal, NavItem} from 'react-bootstrap';
import './css/custommodal.css';
import architecture from '../../architecture.PNG'

class Trigger extends React.Component {
  constructor(props, context) {
    super(props, context);
    this.handleHide = this.handleHide.bind(this);
    this.handleShow = this.handleShow.bind(this);
    this.state = {
      show: false
    };
  }

  handleHide() {
    this.setState({ show: false });
  }

  handleShow() {
   this.setState({ show: true });
 }

  render() {
    return (
      <div className="modal-container">
        <p onClick={this.handleShow}>
          {this.props.label}
        </p>

        <Modal
          show={this.state.show}
          onHide={this.handleHide}
          container={this}
          bsSize="large"
          aria-labelledby="contained-modal-title-lg"
        >
          <Modal.Header closeButton>
            <Modal.Title id="contained-modal-title-lg" style={{color:'black'}}>
              OnTrack - Delay Predictor for Indian Railways
            </Modal.Title>
          </Modal.Header>
          <Modal.Body style={{color:'black'}}>
            <img src='/static/resources/architecture.PNG' className='img-responsive'/>
            Elit est explicabo ipsum eaque dolorem blanditiis doloribus sed id
            ipsam, beatae, rem fuga id earum? Inventore et facilis obcaecati.
            Hello World
          </Modal.Body>
          <Modal.Footer>
            <Button onClick={this.handleHide}>Close</Button>
          </Modal.Footer>
        </Modal>
      </div>
    );
  }
}

export default Trigger
