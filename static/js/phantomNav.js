$(document).ready(function(){
    var $nav = $('.navbar');//Caching element
    $nav.addClass("transparent")
    // fade in .navbar
    $(function () {
        $(window).scroll(function () {
            // set distance user needs to scroll before we start fadeIn
            if ($(this).scrollTop() > 50) { 
                $nav.removeClass("transparent")
            } else if ($(this).scrollTop() < 50){
                $nav.addClass("transparent")
            }
        });
    });

});
