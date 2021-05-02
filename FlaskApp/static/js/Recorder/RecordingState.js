import StoppedState from "./StoppedState.js";
import AudioRecorderState from "./State.js";

class RecordingState extends AudioRecorderState {
  constructor(audioRec) {
    super(audioRec);
  }
  record(callbackFn) {
    console.log("stopButton clicked");
    let rec = this.audioRec.getRecorder();
    //tell the recorder to stop the recording
    rec.stop();
    //stop microphone access
    this.audioRec.getGumStream().getAudioTracks()[0].stop();

    rec.exportWAV((blob) => {
      try {
        callbackFn(blob);
      } catch (err) {
        console.log(err);
      } finally {
        this.audioRec.setState(new StoppedState(this.audioRec));
      }
    });
  }
}

export default RecordingState;
