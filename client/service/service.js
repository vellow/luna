/** 
 * /usr/bin/env node
 *
 **/

var service = require('./invoker');

exports.auth_itebeta = function (username, callback){
  service.auth_itebeta(username, function(res){
    callback(res)
  });
};

exports.auth_uuap = function (username, password, callback){
  service.auth_uuap(username, password, function(res){
    callback(res)
  });
};

exports.get_data = function (serviceUrl, auth, callback){
  service.get_data(serviceUrl, auth, function(res){
    callback(res)
  });
};