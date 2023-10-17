/*
**	SOHU sprots index page main JS
**	author by dongli@sohu-inc.com
*/

(function($){
	var live_container = $('.video'),
		time_container = $('#day-id')
		live_ele = $('.team-video'),//$('.live'),
		video_container = $('#video-cut'),
		live_btn = $('.look-live'),
		live_btn2 = $('#live_btn_2'),
		close_btn = $('.close-icon');

	var opening_time = new Date();
	var controller = {
		initialise : function(){
			opening_time.setFullYear(2014, 5, 12);
			var now = new Date(),
				left_time = Math.floor((opening_time.getTime() - now.getTime())/(1000*3600*24));
			time_container.html(left_time);
		},
		iframeHtml : function(url){
			return '<iframe width="800" height="495" frameborder="0" scrolling="no" id="live_iframe" src="'+ url +'"></iframe>';
		},
		clearIframe : function(){
			$('#live_iframe').remove();
		}
	};

	var bindEvent = function(){
		live_btn.on('click',function(){
			video_container.fadeIn("normal",function(){
				$('#scrollbar').tinyscrollbar();
			});
			live_ele.eq(0).trigger('click');
		});
		live_btn2.click(function(){
			video_container.fadeIn("normal",function(){
				$('#scrollbar').tinyscrollbar();
			});
			live_ele.eq(0).trigger('click');
		});
		close_btn.on('click',function(){
			video_container.fadeOut();
			controller.clearIframe();
		});
		live_ele.on('click',function(){
			var $this = $(this);
			$('.team-video').removeClass('team-video-now');
			$this.closest('.team-video').addClass('team-video-now');
			live_container.html(controller.iframeHtml($this.attr('data')));
		});
	};

	controller.initialise();
	bindEvent();

	$(function(){
		$('#labelC .today').tinyscrollbar();

	/*	$('#labelC .menuC li').eq(0).one('hover',function(){
			$('#labelC .yesterday').tinyscrollbar();
		});*/
		$('#labelC .menuC li:last').one('hover',function(){
			$('#labelC .tomorrow').tinyscrollbar();
		});
	});
})(jQuery)