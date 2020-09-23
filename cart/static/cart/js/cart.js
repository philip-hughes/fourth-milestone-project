$(".adjust-cart").click(function (e) {
    if (($(this).hasClass("increase"))) {
       $(this).siblings('.adjust-type').val('increase');
        $(this).closest('form').submit()
    } else if (($(this).hasClass("decrease"))) {
        $(this).siblings('.adjust-type').val('decrease');
        $(this).closest('form').submit()
    }  else {
        $(this).siblings('.adjust-type').val('remove');
        $(this).closest('form').submit()
        }
});