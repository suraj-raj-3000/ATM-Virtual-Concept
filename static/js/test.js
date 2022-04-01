
function toggle_login(){
    var1 = document.getElementById('admin_form');
    var2 = document.getElementById('login_div');
    var3 = document.getElementById('admin_login_btn');

    if(var1.style.visibility == "visible"){
        var1.style.visibility = "hidden";
        var2.style.visibility = "visible";
        var3.innerHTML = "ADMIN LOGIN";

    }else{
    var1.style.visibility = "visible";
    var2.style.visibility = "hidden";
    var3.innerHTML = "USER LOGIN";
    }
}