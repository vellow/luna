/**
 * node与后台server通讯类
 * @type {*}
 */

var sysConfig = require('../../config.js');
var logger = require('log4js').getLogger('business');
var events = require("events");
var http = require('http');
module.exports = function () {
    function DataServer(options) {
        this.host = sysConfig.SERVER.HOST;   //数据提供端地址
        this.port = sysConfig.SERVER.PORT;
        this.encode = 'UTF-8';
        this.reader = 'JSON';
        this.path = '';
        this.method = 'POST';
        this.reqParam = '';
        this.dataCarrier = null;
        this.isExternal = false;
        this.server_emitter = new events.EventEmitter();
        merge(this, options);
    }
    DataServer.prototype.on = function (eventName, listener) {
        this.server_emitter.on(eventName, listener);
        return this;
    };
    DataServer.prototype.request = function () {
    	var path = '/'+sysConfig.SERVER.CONTEXT+this.path;
    	if (this.isExternal) {
    		path = '/'+this.path;
    	}
        var serverReqOpts = {
            host: this.host,
            port: this.port,
            path: path,
            method: this.method
        };
        var self = this;
        http.globalAgent.maxSockets=50;
        http.globalAgent.defaultMaxSockets=50;
        var serverReq = http.request(serverReqOpts, function (serverRes){
            serverRes.setEncoding('utf8');
            self.dataCarrier = "";
            serverRes.on('data', function (chunk) {
                self.dataCarrier += chunk;
            });
            serverRes.on("close", function(e) {
                console.log("close");
            });
            serverRes.on('end', function () {
                var data =  self.dataCarrier;
                /**
                 *  以后可提取出去作为解析对象使用
                 *  目前只支持JSON
                 */
                if(self.reader.toUpperCase()=='JSON'){
                    try{
                        data = JSON.parse(data);
                    }catch(e){
                        console.error(e);
                    }
                }
                self.server_emitter.emit('response', data);
            });

        });

        // write data to request body
        var sendReqParamStringfy = JSON.stringify(this.reqParam);
        serverReq.write(sendReqParamStringfy);
        logger.info('NODE-Server向'+this.host+':'+this.port+serverReq.path+'发送数据请求！'+this.method+'请求参数：'+sendReqParamStringfy);
        serverReq.end();
        return self;
    };
    return DataServer;
}();

var merge = function (a, b) {
    if (a && b) {
        for (var key in b) {
            a[key] = b[key];
        }
    }
    return a;
};
