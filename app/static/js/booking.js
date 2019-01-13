function showErrorMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

$(document).ready(function(){
    $(".input-daterange").datepicker({
        format: "yyyy-mm-dd",
        startDate: "today",
        language: "zh-CN",
        autoclose: true
    });
    $(".input-daterange").on("changeDate", function(){
        var startDate = $("#start-date").val();
        var endDate = $("#end-date").val();

        if ((startDate && endDate && startDate > endDate) || (startDate && endDate && startDate == endDate)) {
            showErrorMsg("日期有误，请重新选择!");
        } else {
            var sd = new Date(startDate);
            var ed = new Date(endDate);
            days = (ed - sd)/(1000*3600*24);
            var price = $(".house-text>p>span").html();
            var amount = days * parseFloat(price);
            $(".order-amount>span").html(amount.toFixed(2) + "(共"+ days +"晚)");
        }
    });
    var queryData = decodeQuery();
    var houseId = queryData["ids"];

    // 订单提交
    $(".submit-btn").on("click", function () {
        var startDate = $("#start-date").val();
        var endDate = $("#end-date").val();
        var house_id = $("#house_id").val();

        if (!(startDate && endDate)) {
            return
        }

        var params = {
            "start_date": startDate,
            "end_date": endDate,
            "house_id": houseId
        }

        $.ajax({
            url: jsroot+"/api/house_done",
            type: "post",
            headers: {
                "X-CSRFToken": getCookie('csrf_token')
            },
            data: JSON.stringify(params),
            contentType: "application/json",
            success: function (resp) {
                if (resp.status == "0"){
                    location.href = jsroot + "/api/orders?role=custom";
                }else {
                    alert(resp.errmsg)
                    return false
                }
            }
        })
    })
})
