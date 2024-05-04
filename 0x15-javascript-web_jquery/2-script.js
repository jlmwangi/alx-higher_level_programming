//attach a click event handler to the div with id red_header
$('div#red_header').on('click', function() {
	//Update text color of header element when clicked
	$( 'header' ).css('color', '#FF0000');
});
