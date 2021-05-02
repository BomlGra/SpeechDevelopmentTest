import StoppedState from "./StoppedState.js";
import RecordingState from "./RecordingState.js";

class AudioRecorder {
  constructor(constraints) {
    this.state = new StoppedState(this);
    this.constraints = constraints;
    this.gumStream = null;
  }
  record(callbackFn) {
    this.state.record(callbackFn);
  }
  setGumStream(stream) {
    this.gumStream = stream;
  }
  getGumStream() {
    return this.gumStream;
  }
  setState(state) {
    this.state = state;
  }
  getState() {
    return this.state;
  }
  setRecorder(rec) {
    this.recorder = rec;
  }
  getRecorder() {
    return this.recorder;
  }
  getConstraints() {
    return this.constraints;
  }
}

export default AudioRecorder;
