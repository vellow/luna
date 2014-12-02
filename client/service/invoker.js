/** 
 * /usr/bin/env node
 *
 **/

var zerorpc = require('zerorpc');

var client = new zerorpc.Client();

client.connect('tcp://127.0.0.1:4242');

exports.auth_itebeta = function(username, callback){
  client.invoke('auth_itebeta', username, function(error, res, more) {
    console.log('invoke auth_itebeta res: ', res);
    callback(res);
  }); 
};

exports.auth_uuap = function(username, password, callback){
  client.invoke('auth_uuap', username, password, function(error, res, more) {
    console.log('invoke auth_uuap res: ', res);
    callback(res);
  }); 
};

exports.get_data = function(url, auth, callback){
  client.invoke('get_data', url, auth, function(error, res, more) {
    console.log('invoke api res: ', res);
    callback(res);
  });   
}
