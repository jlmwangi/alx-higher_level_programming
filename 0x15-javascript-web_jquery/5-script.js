//adds a li element to a list upon clicking div#add_item
$('div#add_item').on('click', function () {
	//element to be added to ul.my_list
	//element is <li>item</li>
	$('UL.my_list').append('<li>Item</li>');
});
