/** 
 * /usr/bin/env node
 *
 **/

var service = require('./invoker');
var Request = require('../lib/request');

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

exports.get_data = function (serviceUrl, cookies, callback){
  service.get_data(serviceUrl, cookies, function(res){
    callback(res)
  });

  // new Request({
  //   reqUrl: serviceUrl,
  //   cookies: cookies
  // }).request().on('success', function(res){
  //   console.log(res);
  //   callback(res)
  // })

};