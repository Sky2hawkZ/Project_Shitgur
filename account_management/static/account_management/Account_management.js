$(document).ready(function() {
	if($(window).width() > 768){

	// Hide all but first tab content on larger viewports
	$('.accordion__content:not(:first)').hide();

	// Activate first tab
	$('.accordion__title:first-child').addClass('active');

	} else {
	  
	// Hide all content items on narrow viewports
	$('.accordion__content').hide();
	};

	// Wrap a div around content to create a scrolling container which we're going to use on narrow viewports
	$( ".accordion__content" ).wrapInner( "<div class='overflow-scrolling'></div>" );

	// The clicking action
	$('.accordion__title').on('click', function() {
	$('.accordion__content').hide();
	$(this).next().show().prev().addClass('active').siblings().removeClass('active');
	});
	
	// accordion two
	
	function close_accordion_section() {
        $('.accordion_two .accordion_two-section-title').removeClass('active');
        $('.accordion_two .accordion_two-section-content').slideUp(300).removeClass('open');
    }
 
    $('.accordion_two-section-title').click(function(e) {
        // Grab current anchor value
        var currentAttrValue = $(this).attr('href');
 
        if($(e.target).is('.active')) {
            close_accordion_section();
        }else {
            close_accordion_section();
 
            // Add active class to section title
            $(this).addClass('active');
            // Open up the hidden content panel
            $('.accordion_two ' + currentAttrValue).slideDown(300).addClass('open'); 
        }
 
        e.preventDefault();
    });
	
	// Change user image
	
	$( "#change_user_image" ).click(function() {

        alert("Add upload-popup here");

    });
	
});