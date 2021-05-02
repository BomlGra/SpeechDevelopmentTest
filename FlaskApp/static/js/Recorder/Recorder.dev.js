"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

var _StoppedState = _interopRequireDefault(require("./StoppedState.js"));

var _RecordingState = _interopRequireDefault(require("./RecordingState.js"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }

function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); return Constructor; }

var AudioRecorder =
/*#__PURE__*/
function () {
  function AudioRecorder(constraints) {
    _classCallCheck(this, AudioRecorder);

    this.state = new _StoppedState["default"](this);
    this.constraints = constraints;
    this.gumStream = null;
  }

  _createClass(AudioRecorder, [{
    key: "record",
    value: function record(callbackFn) {
      this.state.record(callbackFn);
    }
  }, {
    key: "setGumStream",
    value: function setGumStream(stream) {
      this.gumStream = stream;
    }
  }, {
    key: "getGumStream",
    value: function getGumStream() {
      return this.gumStream;
    }
  }, {
    key: "setState",
    value: function setState(state) {
      this.state = state;
    }
  }, {
    key: "getState",
    value: function getState() {
      return this.state;
    }
  }, {
    key: "setRecorder",
    value: function setRecorder(rec) {
      this.recorder = rec;
    }
  }, {
    key: "getRecorder",
    value: function getRecorder() {
      return this.recorder;
    }
  }, {
    key: "getConstraints",
    value: function getConstraints() {
      return this.constraints;
    }
  }]);

  return AudioRecorder;
}();

var _default = AudioRecorder;
exports["default"] = _default;