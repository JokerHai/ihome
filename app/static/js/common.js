/**
 * Created by joker on 2019/1/13.
 */
function hrefBack() {
    history.go(-1);
}
function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}
/**
 * 解析提取url中的查询字符串参数
 * @returns {*}
 */
function decodeQuery(){
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function(result, item){
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}