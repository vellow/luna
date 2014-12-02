// var hostname = 'http://m1-art-devapp3.vm.baidu.com:8766/oa/';

// exports.api_oa = (function(){
//     return {
//         'getUserInfo': endpoint + 'user/currentUserInfo.do',
//         'getTodo': endpoint + 'user/getTodo.do',
//         'query': endpoint + 'material/query.do?businessType=OFFICE&categoryId=4&officeId=1',
//     }
    
// })()

exports.hostaddr = function(){
    return  'm1-art-devapp3.vm.baidu.com:8766'
}

exports.getUserInfo = function(){
    return '/oa/user/currentUserInfo.do'
}