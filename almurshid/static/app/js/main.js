$(document).ready(function() {

	/* About me slider */
	$('.about-me-slider').slick({
		slidesToShow: 1,
		prevArrow: '<span class="span-arrow slick-prev"><</span>',
		nextArrow: '<span class="span-arrow slick-next">></span>'
	});

	/* Blog slider */
	$('.blog-slider').slick({
		slidesToShow: 2,
		prevArrow: '<span class="span-arrow slick-prev"><</span>',
		nextArrow: '<span class="span-arrow slick-next">></span>',
		responsive: [
		{
			breakpoint: 768,
			settings: {
				slidesToShow: 1
			}
		}
		]
	});

});


var counta = 0;

$(window).scroll(function(e){

	/* Onscroll number counter */
	var statisticNumbers = $('.single-count');
	if(statisticNumbers.length) {
		var oTop = statisticNumbers.offset().top - window.innerHeight;
		if (counta == 0 && $(window).scrollTop() > oTop) {
			$('.count').each(function() {
				var $this = $(this),
				countTo = $this.attr('data-count');
				$({
					countNum: $this.text()
				}).animate({
					countNum: countTo
				},

				{
					duration: 2000,
					easing: 'swing',
					step: function() {
						$this.text(Math.floor(this.countNum));
					},
					complete: function() {
						$this.text(this.countNum);
					}
				});
			});
			counta = 1;
		}
	}

});


$(document).on('submit', 'form.ajax', function(e) {
	console.log("koooi")
	e.preventDefault();
	var $this = $(this);
	var data = new FormData(this);
	var action_url = $this.attr('action');
	var reset = $this.hasClass('reset');
	var reload = $this.hasClass('reload');
	var redirect = $this.hasClass('redirect');
	var redirect_url = $this.attr('data-redirect');

	$.ajax({
		url: action_url,
		type: 'POST',
		data: data,
		cache: false,
		contentType: false,
		processData: false,
		dataType: "json",

		success: function(data) {

			var status = data.status;
			var title = data.title;
			var message = data.message;
			var pk = data.pk;

			if (status == "true") {
				if (title) {
					title = title;
				} else {
					title = "Success";
				}

				Swal.fire({
					title: title,
					text: message,
					icon: 'success',
				}).then(function() {
					if (redirect) {
						window.location.href = redirect_url;
					}
					if (reload) {
						window.location.reload();
					}
					if (reset) {
						window.location.reset();
					}
				});

			} else {
				if (title) {
					title = title;
				} else {
					title = "An Error Occurred";
				}
				Swal.fire({
					title: title,
					text: message,
					icon: "error"
				});

			}
		},
		error: function(data) {
			var title = "An error occurred";
			var message = "something went wrong";
			Swal.fire({
				title: title,
				text: message,
				icon: "error"
			});
		}
	});
});
