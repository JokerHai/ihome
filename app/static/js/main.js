$(function () {

    // 打开登录框
    $('.login_btn').click(function () {
        $.get(jsroot + "/auth/login_view", function (chartHtml) {
            $('.login_form_con').html(chartHtml).show();
        })
    })
    // 打开注册框
    $('.register_btn').click(function () {
        $.get(jsroot + '/auth/register_view', function (chartHtml) {
            $('.register_form_con').html(chartHtml).show();
        });
    })
    $('.shutoff').click(function () {
        $(this).closest('form').hide();
    })
    // 根据地址栏的hash值来显示用户中心对应的菜单
    var sHash = window.location.hash;
    if (sHash != '') {
        var sId = sHash.substring(1);
        var oNow = $('.' + sId);
        var iNowIndex = oNow.index();
        $('.option_list li').eq(iNowIndex).addClass('active').siblings().removeClass('active');
        oNow.show().siblings().hide();
    }

    // 用户中心菜单切换
    var $li = $('.option_list li');
    var $frame = $('#main_frame');

    $li.click(function () {
        if ($(this).index() == 5) {
            $('#main_frame').css({'height': 900});
        }
        else {
            $('#main_frame').css({'height': 660});
        }
        $(this).addClass('active').siblings().removeClass('active');
        $(this).find('a')[0].click()
    })
    function user_mobile_err_content() {
        if (exist_phone_state === false) {
            $("#register-mobile-err").html("请输入中国大陆手机号,其它用户不可见").show();
        }
    }

    // TODO 登录表单提交
    $(".login_form_con").submit(function (e) {
        e.preventDefault()
        var mobile = $(".login_form #mobile").val()
        var password = $(".login_form #password").val()

        if (!mobile) {
            $("#login-mobile-err").show();
            return;
        }

        if (!password) {
            $("#login-password-err").show();
            return;
        }

        // 发起登录请求
        // 拼接参数
        var params = {
            "mobile": mobile,
            "password": password
        }
        /*
         $.ajax({
         url:'/passport/login',
         type:'post',
         data:JSON.stringify(params),
         contentType:'application/json',
         headers:{'X-CSRFToken':getCookie('csrf_token')},
         success: function (resp) {
         //判断是否登陆成功
         if(resp.errno == '0'){
         window.location.reload()
         }else{
         alert(resp.errmsg);
         }

         }
         })
         */
    })
})

//退出登陆
function logout() {
    handledata('post', jsroot + "/auth/logout", '', 'json', '');
    //window.location.reload()
}
// TODO 生成一个图片验证码的编号，并设置页面中图片验证码img标签的src属性
function generateImageCode() {

    var hidden_code_id = $("#image_code_id").val();

    //1.生成一个随机字符串
    imageCodeId = generateUUID();

    //2.拼接图片url地址
    image_url = jsroot + '/auth/captcha_image?cur_id=' + imageCodeId + "&pre_id=" + hidden_code_id

    //3.将地址设置到image标签的src属性中,为image_url
    $('.get_pic_code').attr('src', image_url)

    //4.记录上一次的编号
    if (hidden_code_id != imageCodeId) {
        $("#image_code_id").val(imageCodeId);
    }
}
// 调用该函数模拟点击左侧按钮
function fnChangeMenu(n) {
    var $li = $('.option_list li');
    if (n >= 0) {
        $li.eq(n).addClass('active').siblings().removeClass('active');
        // 执行 a 标签的点击事件
        $li.eq(n).find('a')[0].click()
    }
}

// 一般页面的iframe的高度是660
// 新闻发布页面iframe的高度是900
function fnSetIframeHeight(num) {
    var $frame = $('#main_frame');
    $frame.css({'height': num});
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function generateUUID() {
    var d = new Date().getTime();
    if (window.performance && typeof window.performance.now === "function") {
        d += performance.now(); //use high-precision timer if available
    }
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = (d + Math.random() * 16) % 16 | 0;
        d = Math.floor(d / 16);
        return (c == 'x' ? r : (r & 0x3 | 0x8)).toString(16);
    });
    return uuid;
}
/**
 * 去除空格
 */
function gtrim(txt) {
    if (txt == undefined)
        return "";
    return txt.replace(/(^\s*)|(\s*$)/g, "");
}
function checkTel(mobile) {
    var isPhone = /^([0-9]{3,4}-)?[0-9]{7,8}$/;
    var isMob = /^((\+?86)|(\(\+86\)))?(13[0123456789][0-9]{8}|14[0123456789][0-9]{8}|15[0123456789][0-9]{8}|17[0123456789][0-9]{8}|18[0123456789][0-9]{8}|147[0-9]{8}|1349[0-9]{7}|16[0123456789][0-9]{8}|19[0123456789][0-9]{8})$/;
    if (isMob.test(mobile) || isPhone.test(mobile)) {
        return true;
    } else {
        return false;
    }
}
/**
 * ajax请求封装 add by hd
 */
function handledata(method, dataurl, params, datatype, functionname) {
    jQuery.ajax({
        type: method,
        url: dataurl,
        data: params,
        dataType: datatype,
        headers: {'X-CSRFToken': getCookie('csrf_token')},
        timeout: 200000,
        cache: false,
        error: function (a, b, c) {
            return;
        },
        success: function (data) {
            functionname(data);
        }
    });
}
/**
 *效验密码输入密码必须包含两种规则
 */
function checkPassword(pwd_input) {
    var isPassword = /^(?![A-Z]+$)(?![a-z]+$)(?!\d+$)(?![\W_]+$)\S{6,16}$/;
    if (isPassword.test(pwd_input)) {
        return true;
    } else {
        return false;
    }
}
/* 检查字符的长度是否超出范围
 * @param {type} string 计算的字符名
 * @param {type} length 长度
 * @returns {Boolean}
 */
function check_string_length(string, length) {
    var w = 0;
    var n = 1;
    for (var i = 0; i < string.length; i++) {
        var c = string.charCodeAt(i);
        //单字节加1
        if ((c >= 0x0001 && c <= 0x007e) || (0xff60 <= c && c <= 0xff9f)) {
            w++;
        } else {
            w += 2;
        }
    }
    if (w < n || w > length) {
        return false;
    }
    return true;
}