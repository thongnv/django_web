jQuery(document).ready(function($) {

    $('#slide1').bjqs({
        keyboardnav : true, // enable keyboard navigation
        hoverpause : true, // pause the slider on hover
        automatic  : true,
    });

    $(".gridster ul").gridster({
        widget_margins: [10, 10],
        widget_base_dimensions: [140, 140]
    });

});