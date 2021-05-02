//webkitURL is deprecated but nevertheless
URL = window.URL || window.webkitURL;

import AudioRecorder from "./Recorder/Recorder.js";
import RecordSender from "./Sender.js";
import RecordStorage from "./Storage.js";

// shim for AudioContext when it's not avb.
var AudioContext = window.AudioContext || window.webkitAudioContext;
var recordButton = document.getElementById("recordButton");
var listenButton = document.getElementById("listen");
var nextButton = document.getElementById("next");

let audioRec = new AudioRecorder({ audio: true, video: false });
let sender = new RecordSender("/");
let storage = new RecordStorage();

recordButton.addEventListener("click", () => {
  audioRec.record((record) => {
    storage.add(record);
  });
});

nextButton.addEventListener("click", () => {
  const records = storage.getRecords();
  sender
    .send(records)
    .then(() => {
      storage.clear();
    })
    .catch((err) => {
      console.log(err);
    });
});
