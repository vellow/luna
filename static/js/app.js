/**
 * Created by YellowGlue on 6/16/15.
 */

 var userIpt = document.getElementById('userIpt');
    var urlIpt = document.getElementById('urlIpt');
    var ruleIpt = document.getElementById('ruleIpt');
    var ruleForm = document.getElementById('ruleForm');
    var mockData = document.getElementById('mockData');
    function fetch_real_data(){
      var xhr = new XMLHttpRequest();
      xhr.responseType='json';
      var url = 'http://' + location.host + '/real?isMock=false&user=' + userIpt.value + '&service=' + urlIpt.value;
      xhr.onreadystatechange = function(){
         if(xhr.readystate === 4 || xhr.status === 200){
            res = xhr.response
            realData.innerHTML = JSON.stringify(res)
            mockData.innerHTML = ""
         }
      }
      xhr.open("GET",url,true);
      xhr.send(null);
    }

    function fetch_mocked_data(){
      var xhr = new XMLHttpRequest();
      xhr.responseType='json';
      var url = 'http://' + location.host + '/mock';
      xhr.onreadystatechange = function(){
         if(xhr.readystate === 4 || xhr.status === 200){
            res = xhr.response
            mockData.innerHTML = JSON.stringify(res)
            realData.innerHTML = ""
         }
      }
      xhr.open("POST",url,true);
      xhr.send(new FormData(ruleForm));
    }
    function fetch_rule(url){
      var xhr = new XMLHttpRequest();
      xhr.responseType='json';
      url = 'http://' + location.host + '/search?url=' + url;
      xhr.onreadystatechange = function(){
         if((xhr.readystate === 4 || xhr.status === 200) && xhr.response){
            res = xhr.response;
            urlIpt.value = res.data['url'];
            ruleIpt.value = res.data['rule'];
         }
      }
      xhr.open("GET",url,true);
      xhr.send(null);
    }
    function save_rule(){
      var xhr = new XMLHttpRequest();
      xhr.responseType='json';
      var url = 'http://' + location.host + '/line/save';
      xhr.onreadystatechange = function(){
         if(xhr.readystate === 4 || xhr.status === 200){
            window.location.reload()
         }
      }
      xhr.open("POST",url,true);
      xhr.send(new FormData(ruleForm));
    }
    function delete_rule(url){
      var xhr = new XMLHttpRequest();
      xhr.responseType='json';
      var url = 'http://' + location.host + '/line/remove?url=' + url;
      var thisLi = event.target.parentNode
      xhr.onreadystatechange = function(){
         if(xhr.readystate === 4 || xhr.status === 200){
            window.location.reload()
         }
      }
      xhr.open("GET",url,true);
      xhr.send(null);
    }