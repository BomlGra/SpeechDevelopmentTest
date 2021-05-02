import AudioRecorderState from "./State.js";
import RecordingState from "./RecordingState.js";

class StoppedState extends AudioRecorderState {
  constructor(audioRec) {
    super(audioRec);
  }
  record(_) {
    console.log("recordButton clicked");

    navigator.mediaDevices
      .getUserMedia(this.audioRec.getConstraints())
      .then((stream) => {
        console.log(
          "getUserMedia() success, stream created, initializing Recorder.js ..."
        );

        let audioContext = new AudioContext();
        this.audioRec.setGumStream(stream);

        /* use the stream */
        let input = audioContext.createMediaStreamSource(stream);
        this.audioRec.setRecorder(
          new Recorder(input, {
            numChannels: 1,
          })
        );

        //start the recording process
        this.audioRec.getRecorder().record();
        console.log("Recording started");
        this.audioRec.setState(new RecordingState(this.audioRec));
      })
      .catch(function (err) {
        //enable the record button if getUserMedia() fails
        console.log(err);
      });
  }
}

export default StoppedState;
