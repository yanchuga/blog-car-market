jQuery(document).ready(function($){
			var from_year = '';
			var to_year = '';
			$("#from_year").change(function () {
					var val = $("#from_year").val();
					// console.log(from_year);
					from_year = val;
				});
			$("#to_year").change(function () {
					var val = $("#to_year").val();
					to_year = val;
					// console.log(to_year);
				});
		$('#filter_btn').click(function() {
					if (from_year && to_year)
					{
						str = '?from_year=' + from_year + '&to_year=' + to_year;
					}
					else if (from_year)
					{
						str = '?from_year=' + from_year;
					}
					else if (to_year)
					{
						str = '?to_year=' + to_year;
					}
					else
					{
						console.log('choose smth');
					}
					str = 'http://127.0.0.1:8000/' + str;
					window.open(str);
		});
    });