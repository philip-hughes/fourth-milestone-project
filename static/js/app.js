;(function($){
    $.fn.scrollPosReaload = function(){
        if (localStorage) {
            var posReader = localStorage["posStorage"];
            if (posReader) {
                $('html').css('scroll-behavior', 'auto')
                $(window).scrollTop(posReader);
                $('html').css('scroll-behavior', 'smooth')
                localStorage.removeItem("posStorage");
            }
            $(this).click(function(e) {
                localStorage["posStorage"] = $(window).scrollTop();
            });
            return true;
        }
        return false;
    }
    $(document).ready(function() {
        if ( $( "#bottom-header" ).length ) {
                $(".content-wrapper").css('padding-top', '153px')
            }
        else {
                $(".content-wrapper").css('padding-top', '103px')
        }   

        $('.item-submit').scrollPosReaload();
        
    });
}(jQuery));  