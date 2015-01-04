/**
 * node-server通讯类
 * @type {*}
 */

var logger = require('log4js').getLogger('business');
var events = require("events");
var http = require('http');
var url = require('url');

module.exports = function() {
  function DataServer(options) {
    this.reqUrl = '';
    this.method = 'GET';
    this.reqParam = '';
    this.cookies = '';
    this.server_emitter = new events.EventEmitter();
    merge(this, options);
  }
  DataServer.prototype.on = function(eventName, listener) {
    this.server_emitter.on(eventName, listener);
    return this;
  };
  DataServer.prototype.request = function() {
    var pUrl = url.parse(this.reqUrl);
    var reqOpts = {
      host: pUrl.hostname,
      port: pUrl.port,
      path: pUrl.path,
      headers: {'Cookie': this.cookies},
      method: this.method
    };
    var self = this;
    http.globalAgent.maxSockets = 50;
    http.globalAgent.defaultMaxSockets = 50;
    var req = http.request(reqOpts, function(serverRes) {
      serverRes.setEncoding('utf8');
      self.body = "";
      self.headers = serverRes.headers;
      serverRes.on('data', function(chunk) {
        self.body += chunk;
      });
      serverRes.on("close", function(e) {
        console.log("close");
      });
      serverRes.on('end', function() {
        self.server_emitter.emit('success', {headers: self.headers, body: self.body});
      });

    });

    if (this.reqParam) {
      var sendReqParamStringfy = JSON.stringify(this.reqParam);
      req.write(sendReqParamStringfy);
      logger.info('NODE-Server向' + this.reqUrl + '发送 ' + this.method + ' 请求,  请求参数：' + sendReqParamStringfy);
    }

    logger.info('NODE-Server向' + this.reqUrl + '发送 ' + this.method + ' 请求');

    req.end();
    return self;
  };
  return DataServer;
}();

var merge = function(a, b) {
  if (a && b) {
    for (var key in b) {
      a[key] = b[key];
    }
  }
  return a;
};