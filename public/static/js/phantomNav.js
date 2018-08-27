$(document).ready(function(){
    var $nav = $('.nav');//Caching element
    // fade in .navbar
    $(function () {
        $(window).scroll(function () {
            // set distance user needs to scroll before we start fadeIn
            if ($(this).scrollTop() > 100) { //For dynamic effect use $nav.height() instead of '100'
                $nav.removeClasss("transparent")
            } else if ($(this).scrollTop() < 100){
                $nav.addClass("transparent")
            }
        });
    });

});
