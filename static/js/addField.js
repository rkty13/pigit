$(document).ready(function(){
	var maxFields = 8;
	var wrapper = $(".input_fields");
	var addButton = $(".add_field");

	var i = 1;
	$(addButton).click(function(e){
		e.preventDefault();
		if(i < maxFields){
			i++;
			$(wrapper).append('<div><input type="text" name="users'+i+'"/> <a href="#" class="remove_field">Remove</a></div>');
		}
	});

	$(wrapper).on("click", ".remove_field", function(e){
		e.preventDefault();
		$(this).parent('div').remove();
		x--;
	});
});