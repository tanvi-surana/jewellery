var load_form2 = function(){
  var req = new XMLHttpRequest();
  baseurl = window.location.origin;
  req.open("GET",baseurl+"/accounts/login-signup/",true);
  req.setRequestHeader("X-Requested-With","XMLHttpRequest");
  req.responseType = 'document';
  req.send();
  $(req).load(function(){
    console.log(req.response);
  });
}

$(document).ready(function(){
  account_circle = $(".page .navBar .wrapper .dock ul li div.account");
  user_icon = $(".page .navBar .wrapper .dock ul li i");
  account_circle.click(function call_load() {
    load_form2();
  });
  user_icon.click(function call_load(){
    load_form2();
  });
});
  