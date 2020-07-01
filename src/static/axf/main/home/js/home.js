$(function(){
    init_mySwiper();
    init_mySwiper1()
})
function init_mySwiper() {
    var mySwiper = new Swiper ('#topSwiper', {
        loop:true,
        autoplay:3000,
        //自动播放互动时禁用
        autoplayDisableOnInteraction:false,
        //分页器
        pagination: '.swiper-pagination',
    })

}
function init_mySwiper1() {
    var mySwiper = new Swiper('#swiperMenu',{
       slidesPerView:3,
    })

}