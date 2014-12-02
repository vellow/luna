/** 
 * /usr/bin/env node
 *
 **/

var uuid = require('node-uuid');

exports.gen_uuid = function(){
  return uuid.v4()   
};

exports.parse_cookies = function (request) {
    var list = {},
        rc = request.headers.cookie;

    rc && rc.split(';').forEach(function( cookie ) {
        var parts = cookie.split('=');
        list[parts.shift().trim()] = unescape(parts.join('='));
    });

    return list;
};
