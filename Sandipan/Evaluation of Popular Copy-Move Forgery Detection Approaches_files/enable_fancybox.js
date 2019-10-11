jQuery.noConflict(); 
jQuery(document).ready(function() { 
 jQuery('a.lightbox').fancybox({ 
  'titlePosition' : 'inside', 
  'overlayColor' : '#AAA', 
  'overlayOpacity' : '0.5', 
  'hideOnContentClick' : 'true', 
  'speedIn' : '100', 
  'speedOut' : '100', 
  'transitionIn' : 'fade', 
  'transitionOut' : 'elastic'
 });
 
 var animationDuration = 200;
 var $titleDivs = '.phd-gallery .thumbnails .thumbnail div.title';
 var $thumbnailDivs = '.phd-gallery .thumbnails .thumbnail';
 
 jQuery($titleDivs).hide();
 jQuery($thumbnailDivs).hover(function() {
		jQuery('div.title', this).slideDown(animationDuration);
 	}, function() {
		jQuery('div.title', this).slideUp(animationDuration);
	});

 jQuery('.phd-gallery .thumbnails a.more').fancybox({
 	'centerOnScroll' : 'true'
 });
 
 jQuery('.univis2web .mail').bind({
  	mouseenter: function() {
  	   var elem = this;
  	   var univisKey = jQuery(this).attr("rel");
  	  
  	   if (jQuery(this).attr('active') != '1')
  	   {
  	   	   jQuery(this).attr('active', '1');
	  
	  	   jQuery.ajax({
	    		type: "GET",
	    		crossDomain: true,
	    		url: "index.php",
	    		dataType: 'html',
	    		data: {
	    				eID: 'univis2web_changeMail', 
	    				key: univisKey
	    		},
	    		
	    		success: function(html){
        			jQuery('div.con', elem).hide().html(html).fadeIn(200);
        		}
        		
    		});
    		setTimeout(function() {
                    jQuery(elem).removeAttr('active');
                    
            }, 1000);
    	}
  	},
  	mouseout: function() {
  			jQuery('div.con','.univis2web .mail').html('<img width="24" height="24" src="images/email.gif">');
  	  	
  	}
  });
});


/*
$(function() {
	var animationDuration = 200;
	var $titleDivs = $(".phd-gallery .thumbnails .thumbnail div.title");
	var $thumbnailDivs = $(".phd-gallery .thumbnails .thumbnail");
	//$thumbnailDivs.css("cursor", "pointer");
	$titleDivs.hide();
	
	$thumbnailDivs.hover(function() {
		var $this = this;
		var $titleDiv = $('div.title', $this);
		$titleDiv.slideDown(animationDuration);
	}, function() {
		var $this = this;
		var $titleDiv = $('div.title', $this);
		$titleDiv.slideUp(animationDuration);
	});
	
	$(".phd-gallery .thumbnails a.more").fancybox({
	});
}); 
*/
