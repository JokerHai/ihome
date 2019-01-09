/**
 *  注册相关js
 * Created by joker on 2019/1/2.
 */
var bind_click_times = 0;
var exist_nick_name_state = false;
var exist_phone_state = false;
var exist_image_code_state = false;
var exist_code_pwd_state = false;
var exist_register_password = false;
function user_mobile_err_content() {
    if (exist_phone_state === false) {
        $("#register-mobile-err").html("请输入中国大陆手机号,其它用户不可见").show();
    }
}
function user_imageCaptchaValue_err_content() {
    if (exist_image_code_state === false) {
        $("#user_imageCaptcha_err").html("请输入验证码，不区分大小写").show();
    }
}
function user_code_pwd_err_content() {
    if (exist_code_pwd_state === false) {
        $("#register-sms-code-err").html("请输入获取的6位校验码").show();
    }
}
function user_register_password_err_content() {
    if (exist_register_password === false) {
        $("#register-password-err").html("请输入8-16位密码，数字、字母和符号至少包含两种").show();
    }
}
function user_nick_name_err_content() {
    if (exist_nick_name_state === false) {
        $("#register-nick-name-err").html("不超过7个汉字或者14个字母和符号").show();
    }
}
/**
 * 检查名字名称
 * @param {type Boolean} is_submit
 * @returns {Boolean}
 */
function check_nick_name(is_submit) {
    var nick_name = gtrim($("#user_nick_name").val());
    if (nick_name.length <= 0) {
        if (is_submit) {
            $("#register-nick-name-err").show();
            $("#register-nick-name-err").html("不超过7个汉字或者14个字母和符号");
            return false
        } else {
            $("#register-nick-name-err").hide();
            $("#register-nick-name-err").html("");
            exist_nick_name_state = true;
        }
    } else if (check_string_length(nick_name, 14) === false) {
        $("#register-nick-name-err").show();
        $("#register-nick-name-err").html("不超过7个汉字或者14个字母和符号");
        return false;
    } else {
        $("#register-nick-name-err").hide();
        $("#register-nick-name-err").html("");
        exist_nick_name_state = true;
    }
}
/**
 * 检查手机号是否合法
 * @param {type Boolean} is_submit
 * @returns {Boolean}
 */
function check_mobile(is_submit) {
    //验证手机号码格式   checkTel
    var register_mobile = gtrim($("#register_mobile").val());
    if (register_mobile.length <= 0) {
        if (is_submit) {
            $("#register-mobile-err").show();
            $("#register-mobile-err").html("请输入您的手机号");
            return false;
        } else {
            $("#register-mobile-err").hide();
            $("#register-mobile-err").html("");
            return true;
        }

    } else if (checkTel(register_mobile) === false) {
        $("#register-mobile-err").show();
        $("#register-mobile-err").html("手机格式不正确");
        return false;
    } else if (is_submit === false) {
        var params = "identity=" + encodeURIComponent(register_mobile);
        handledata('post', jsroot + "/auth/check_mobile", params, 'json', showMessage);
        return true;
    }

}
/**
 * 效验图片验证码
 */
function check_image_captcha(is_submit) {
    var cellImageCaptcha = gtrim($("#imageCaptchaValue").val());
    var hidden_code_id = $("#image_code_id").val();
    if (cellImageCaptcha.length <= 0) {
        if (is_submit) {
            $("#user_imageCaptcha_err").show();
            $("#user_imageCaptcha_err").html("请输入验证码，不区分大小写");
            return false;
        } else {
            $("#user_imageCaptcha_err").hide();
            $("#user_imageCaptcha_err").html("");
            return true;
        }
    } else if (is_submit === false) {
        var params = "image_captcha=" + encodeURIComponent(cellImageCaptcha) + "&image_code_id=" + encodeURIComponent(hidden_code_id);
        handledata('post', jsroot + "/auth/check_image_captcha", params, 'json', callResults);
        return true;
    }
}
/**
 * 效验手机验证码
 * @param msg_back
 */
function check_code_pwd(is_submit) {
    var sms_code = gtrim($("#sms_code").val());
    var register_mobile = gtrim($("#register_mobile").val());
    if (sms_code.length <= 0) {
        if (is_submit) {
            $("#register-sms-code-err").show();
            $("#register-sms-code-err").html("请输入获取的6位校验码");
            return false;
        } else {
            $("#register-sms-code-err").hide();
            $("#register-sms-code-err").html("");
            return true;
        }
    } else if (is_submit === false) {
        var params = "sms_code=" + encodeURIComponent(sms_code) + "&register_mobile=" + encodeURIComponent(register_mobile);
        handledata('post', jsroot + "/auth/check_msg_pwd", params, 'json', call_mag_pwd_results);
        return true;
    }
}
/**
 * 获取密码
 * @param {type Boolean} is_submit
 */
function check_pwd(is_submit) {
    var user_password = gtrim($("#register_password").val());
    if (user_password.length <= 0) {
        if (is_submit) {
            $("#register-password-err").show();
            $("#register-password-err").html("请输入密码");
            return false;
        } else {
            $("#register-password-err").hide();
            $("#register-password-err").html("");
            exist_register_password = true;
            return true;
        }
    } else if (user_password.length < 6 && user_password.length >= 0) {
        $("#register-password-err").show();
        $("#register-password-err").html("密码长度必须大于6位");
        return false;
    } else if (user_password.length > 16) {
        $("#register-password-err").show();
        $("#register-password-err").html("密码长度为不能超过16位");
        return false;
    } else if (checkPassword(user_password) === false) {
        $("#register-password-err").show();
        $("#register-password-err").html("密码设置过于简单");
        return false;
    } else {
        $("#register-password-err").hide();
        $("#register-password-err").html("");
        exist_register_password = true;
        return true;
    }
}
//验证手机回调函数
function showMessage(msg_back) {
    if (msg_back.status == "0") {
        $("#register-mobile-err").hide();
        $("#register-mobile-err").html("");
        exist_phone_state = true;
    } else {
        $("#register-mobile-err").html(msg_back.errmsg);
        exist_phone_state = false;
    }
}
function callResults(msg_back) {
    if (msg_back.status == "0") {
        $("#user_imageCaptcha_err").hide();
        $("#user_imageCaptcha_err").html("");
        exist_image_code_state = true;
    } else {
        $("#user_imageCaptcha_err").show();
        $("#user_imageCaptcha_err").html(msg_back.errmsg);
    }
}
function call_mag_pwd_results(msg_back) {
    if (msg_back.status == "0") {
        $("#user_imageCaptcha_err").hide();
        $("#register-sms-code-err").html("");
        exist_code_pwd_state = true;
    } else {
        $("#register-sms-code-err").html(msg_back.errmsg);
    }
}
// 发送短信验证码
function sendSMSCode() {
    // 校验参数，保证输入框有数据填写
    //移除按钮点击事件
    var hidden_code_id = $("#image_code_id").val();
    $(".get_code").removeAttr("onclick");
    var mobile = $("#register_mobile").val();
    if (!mobile) {
        $("#register-mobile-err").html("请输入中国大陆手机号,其它用户不可见");
        $("#register-mobile-err").show();
        $(".get_code").attr("onclick", "sendSMSCode();");
        return;
    }
    var imageCaptchaValue = $("#imageCaptchaValue").val();
    if (!imageCaptchaValue) {
        $("#user_imageCaptcha_err").html("请输入验证码，不区分大小写");
        $("#user_imageCaptcha_err").show();
        $(".get_code").attr("onclick", "sendSMSCode();");
        return;
    }

    // TODO 发送短信验证码
    //拼接参数
    var params = {
        "mobile": mobile,
        "image_code": imageCaptchaValue,
        "image_code_id": hidden_code_id
    }
    console.log(params)
    //发送获取短信请求

    $.ajax({
        url: jsroot + '/auth/sms_code',//请求地址
        type: 'post',
        data: JSON.stringify(params),
        contentType: 'application/json',
        headers: {'X-CSRFToken': getCookie('csrf_token')},
        success: function (resp) {
            //判断是否请求成功
            if (resp.status == '0') {

                //定义倒计时时间
                var num = 60;

                //创建定时器
                var t = setInterval(function () {

                    //判断是否倒计时结束
                    if (num == 1) {
                        //清除定时器
                        clearInterval(t)
                        //设置标签点击事件,并设置内容
                        $(".get_code").attr("onclick", 'sendSMSCode()');
                        $(".get_code").html('点击获取验证码');


                    } else {
                        //设置秒数
                        num -= 1;
                        $('.get_code').html(num + '秒');
                    }
                }, 1000);//一秒走一次

            } else {//发送失败
                // 重新设置点击事件,更新图片验证码
                $(".get_code").attr("onclick", 'sendSMSCode()');
                generateImageCode();
            }
        }
    })
}
function cl() {
    var checked_len = $("input[name='gc_vip']:checked").length;
    if (checked_len) {
        $("#gc_vip_error").hide();
        $("#gc_vip_error").html("");
        return true;
    } else {
        $("#gc_vip_error").show();
        $("#gc_vip_error").html("同意使用条款，并已阅读\"跟帖评论自律管理承诺书\"");
    }
}
$(function () {
    $('.shutoff').click(function () {
        $(this).closest('form').hide();
    })
    // // 登录框和注册框切换
    // $('.to_login').click(function () {
    //     $('.login_form_con').show();
    //     $('.register_form_con').hide();
    // })
    generateImageCode()
})
function ch_value(signup_key) {
    if (bind_click_times > 0) {
        alert('请稍等，正在处理中...')
        return false;
    }
    bind_click_times = 1;
    var params = '';
    var data_url = jsroot + '/auth/register';
    check_nick_name(true);
    check_mobile(true);
    check_image_captcha(true);
    check_code_pwd(true);
    check_pwd(true)
    cl();
    var state = exist_phone_state && exist_image_code_state && exist_code_pwd_state && exist_register_password && exist_nick_name_state;
    if (state) {
        var user_nick_name = $("#user_nick_name").val();
        console.log(user_nick_name);
        var mobile = $("#register_mobile").val();
        var imageCaptchaValue = $("#imageCaptchaValue").val();
        var sms_code = $("#sms_code").val()
        var user_password = $("#register_password").val();
        params = "mobile=" + encodeURIComponent(mobile) + "&sms_code="
            + encodeURIComponent(sms_code) + "&user_password=" + user_password + "&user_nick_name=" + encodeURIComponent(user_nick_name)
        handledata('post', data_url, params, 'json', register_response);
    } else {
        bind_click_times = 0;
        return state;
    }
    return state;
}
/**
 * 注册回调函数
 */
function register_response(msg_back) {
    if (msg_back.status == "0") {
        window.location.reload();
    } else {
        alert(msg_back.errmsg);
        return false;
    }
}
