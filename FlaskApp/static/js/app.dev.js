"use strict";

var _Recorder = _interopRequireDefault(require("./Recorder/Recorder.js"));

var _Sender = _interopRequireDefault(require("./Sender.js"));

var _Storage = _interopRequireDefault(require("./Storage.js"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

//webkitURL is deprecated but nevertheless
URL = window.URL || window.webkitURL;
// shim for AudioContext when it's not avb.
var AudioContext = window.AudioContext || window.webkitAudioContext;
var recordButton = document.getElementById("recordButton");
var listenButton = document.getElementById("listen");
var nextButton = document.getElementById("next");
var audioRec = new _Recorder["default"]({
  audio: true,
  video: false
});
var sender = new _Sender["default"]("/");
var storage = new _Storage["default"]();
recordButton.addEventListener("click", function () {
  audioRec.record(function (record) {
    storage.add(record);
  });
});
nextButton.addEventListener("click", function () {
  var records = storage.getRecords();
  sender.send(records).then(function () {
    storage.clear();
  })["catch"](function (err) {
    console.log(err);
  });
});