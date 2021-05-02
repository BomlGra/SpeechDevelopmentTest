"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }

function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); return Constructor; }

var RecordSender =
/*#__PURE__*/
function () {
  function RecordSender(url) {
    _classCallCheck(this, RecordSender);

    this.url = url;
  }

  _createClass(RecordSender, [{
    key: "send",
    value: function send(records) {
      var data;
      return regeneratorRuntime.async(function send$(_context) {
        while (1) {
          switch (_context.prev = _context.next) {
            case 0:
              console.log(records);

              if (!(records.length == 0)) {
                _context.next = 3;
                break;
              }

              throw new Error('No records');

            case 3:
              data = new FormData();
              records.forEach(function (record, i) {
                console.log("index ".concat(i, ": ").concat(record));
                data.append("records[]", record, "record_".concat(i));
              });
              _context.next = 7;
              return regeneratorRuntime.awrap(fetch(this.url, {
                method: "POST",
                body: data
              }));

            case 7:
              return _context.abrupt("return", _context.sent);

            case 8:
            case "end":
              return _context.stop();
          }
        }
      }, null, this);
    }
  }]);

  return RecordSender;
}();

var _default = RecordSender;
exports["default"] = _default;