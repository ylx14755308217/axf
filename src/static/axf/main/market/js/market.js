//标签对象 事件
//事件
//$(this)代表是当前的点击对象$('#all_type')
//toggleClass() 会将两个样式进行交互替换
$(function () {
    $('#all_type').click(function () {
        $(this).find('span').toggleClass('glyphicon glyphicon-chevron-down glyphicon glyphicon-chevron-up');
        $('#all_type_container').toggle();
    })

    $('#sort_rule').click(function () {
        $(this).find('span').toggleClass('glyphicon glyphicon-chevron-down glyphicon glyphicon-chevron-up')
        $('#sort_rule_container').toggle();
    })
})