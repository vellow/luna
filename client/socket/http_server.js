/** 
 * /usr/bin/env node
 *
 **/

var http = require('http');
var utils = require('../lib/utils');
var url = require('url');
var service = require('../service/service');
var resUtils = require('../service/response');

var cookieCache = {};

http.createServer(function (req, response) {
  var reqQuery = url.parse(req.url, true).query;
  var reqCookie = utils.parse_cookies(req);
  if( reqQuery['user'] || cookieCache.hasOwnProperty(reqCookie['MIDUUID']) === false ){
    service.auth_itebeta(reqQuery['user'], function(auth){
      cookieCache[miduuid] = auth;
      service.get_data(reqQuery['service'], auth, function(data){
        resUtils.do_response(response, miduuid, data)
      })
    });
    var miduuid = utils.gen_uuid();
  } else {
      var auth = cookieCache[reqCookie['MIDUUID']];
      service.get_data(reqQuery['service'], auth, function(data){
        resUtils.do_response(response, '',data)     
      })
  }

}).listen(1337, '172.22.230.75');


console.log('Server running at http://127.0.0.1:1337/');
