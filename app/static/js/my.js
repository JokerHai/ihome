function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

// 点击推出按钮时执行的函数
function logout() {
    $.get(jsroot+"/auth/logout",function (resp) {
        if(resp.status == "0"){
            location.href = jsroot
        }
    })
}

$(document).ready(function(){

    // 在页面加载完毕之后去加载个人信息
    $.get("/api//user_index", function (resp) {
        if (resp.errno == "0") {
            // 设置数据
            $("#user-avatar").attr("src", resp.data.avatar_url)
            $("#user-name").html(resp.data.name)
            $("#user-mobile").html(resp.data.mobile)
        }else if (resp.errno == "4101") {
            location.href = "/login.html"
        }else {
            alert(resp.errmsg)
        }
    })

});
