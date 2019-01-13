// // 解析提取url中的查询字符串参数
// function decodeQuery(){
//     var search = decodeURI(document.location.search);
//     return search.replace(/(^\?)/, '').split('&').reduce(function(result, item){
//         values = item.split('=');
//         result[values[0]] = values[1];
//         return result;
//     }, {});
// }

$(document).ready(function(){
        var mySwiper = new Swiper ('.swiper-container', {
        loop: true,
        autoplay: 2000,
        autoplayDisableOnInteraction: false,
        pagination: '.swiper-pagination',
        paginationType: 'fraction'
    });
    // // 获取详情页面要展示的房屋编号
    // var queryData = decodeQuery();
    // var houseId = queryData["id"];
    //
    // // 获取该房屋的详细信息
    // $.get(jsroot+'/api/house_detail?='+houseId, function (resp) {
    //     var html = "";
    //     if (resp.status == "0") {
    //         // 1. 显示房屋顶部图片
    //         html += '<ul class="swiper-wrapper">';
    //         for(var i = 0; i<resp.data.house.img_urls.length;i++){
    //             html += '<li class="swiper-slide"><img src="'+resp.data.house.img_urls[i]+'"></li>'
    //         }
    //          html += '</ul>';
    //          html += '<div class="swiper-pagination"></div>'+
    //                  '<div class="house-price">￥<span>'+resp.data.house.price/100.0+'</span>/晚</div>';
    //         $(".swiper-container").html(html);
    //         // 数据加载完毕后,需要设置幻灯片对象，开启幻灯片滚动
    //
    //         //
    //         // // 2. 显示房屋详情内容
    //         // $(".detail-con").html(template("house-detail-tmpl", {"house": resp.data.house}))
    //         // // 3. 处理底部的预订按钮，如果当前用户不是房东的话，就显示预订按钮
    //         // if (resp.data.user_id != resp.data.house.user_id) {
    //         //     $(".book-house").show()
    //         //     $(".book-house").attr("href", "/booking.html?hid="+houseId)
    //         // }
    //     }
    // })
    
})
function reservation(ids) {
    window.location.href = jsroot+"/api/house_done?ids="+ids;
}