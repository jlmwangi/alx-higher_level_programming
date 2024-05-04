//toggles the class header on clicking div#toggle_header
$('div#toggle_header').on('click', function () {
	//update class to green or red on clicking div_toggleheader
	//must always have one class, nevr both and never empty
	if ($('header').hasClass('red')) {
		$('header').removeClass('red').addClass('green');
	}
	else {
		$('header').removeClass('green').addClass('red');
	}
});
