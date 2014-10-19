$(function() {
    $("[data-toggles]").click(function(evt) {
        evt.preventDefault();
        $(this.getAttribute("data-toggles")).slideToggle('slow');
    });
});