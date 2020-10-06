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
        console.log('document ready')
        if ( $( "#bottom-header" ).length ) {
                console.log('applying content style')
                $(".content-wrapper").css('padding-top', '153px')
                $(".content-wrapper").css('min-height', 'calc(100vh - 150px)')
                /*150px = footer height*/
            }
        else {
                $(".content-wrapper").css('padding-top', '103px')
                $(".content-wrapper").css('min-height', 'calc(100vh - 150px)')
                /*150px = footer height*/
        }   

        $('.item-submit').scrollPosReaload();
        
    });
}(jQuery));  