var Request = require('../lib/request');

new Request({
  reqUrl: 'http://localhost:8000',
  headers: {Cookies: 'TGC=disafuiogau'}
}).request().on('success', function(response){
  console.log('response: ');
  console.log(response);
})