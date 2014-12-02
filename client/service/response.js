/**
 * make response
 */


exports.do_response = function (response, miduuid, data){
  var resHeaders = {
    'Content-Type': 'application/json;charset=UTF-8'
  };
  if(miduuid){
    resHeaders['Set-Cookie'] = 'MIDUUID=' + miduuid
  }
  response.writeHead(200, resHeaders);
  response.end(JSON.stringify(data));        
};
