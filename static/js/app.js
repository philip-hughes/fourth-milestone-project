(function ($) {

    /* Code to maintain scroll position on menu screen when items are add to cart */
  $.fn.scrollPosReaload = function () {
    if (localStorage) {
      var posReader = localStorage["posStorage"];
      if (posReader) {
        $("html").css("scroll-behavior", "auto");
        $(window).scrollTop(posReader);
        $("html").css("scroll-behavior", "smooth");
        localStorage.removeItem("posStorage");
      }
      $(this).click(function (e) {
        localStorage["posStorage"] = $(window).scrollTop();
      });
      return true;
    }
    return false;
  };
  $(document).ready(function () {

        /*Adjust content wrapper height according to whether the bottom header is displayed or not */
    if ($("#bottom-header").length) {
      $(".content-wrapper").css("padding-top", "129px");
      $(".content-wrapper, #select-store-wrapper").css(
        "min-height",
        "calc(100vh - 150px)"
      );
      /*150px = footer height*/
    } else {
      $(".content-wrapper").css("padding-top", "80px");
      $(".content-wrapper, #select-store-wrapper").css(
        "min-height",
        "calc(100vh - 150px)"
      );
      /*150px = footer height*/
    }

    $(".item-submit").scrollPosReaload();

    /* Toggling this class controls the z-index of the menu section links so they dont interfere with the 
       nav dropdown in small screens*/
    $("#dropdown-button").click(function () {
         $("#section-link-container").toggleClass('visible')
      $("#dropdown-menu").toggle("fast", function () {
      }
      );
    });
    
  });
})(jQuery);
