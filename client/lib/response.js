/**
 * make response
 */


exports.do_response = function (response, miduuid, data){
  var resHeaders = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Connection': 'close',
    'Access-Control-Allow-Origin': '*'
  };
  if(miduuid){
    resHeaders['Set-Cookie'] = 'MIDUUID=' + miduuid
  }
  response.writeHead(200, resHeaders);
  response.end(data);        
};
