;(function($){
    $.fn.scrollPosReaload = function(){
        if (localStorage) {
            var posReader = localStorage["posStorage"];
            if (posReader) {
                $(window).scrollTop(posReader);
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
        $('.item-submit').scrollPosReaload();
    });
}(jQuery));  