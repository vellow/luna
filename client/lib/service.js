/**
 * /usr/bin/env node
 */
var http = require('http');

exports.request = function(options, cal){
    var cal = cal || function(){};
    return http.get(options, cal)
}