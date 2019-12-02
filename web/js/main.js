$(document).ready(function() {

  'use strict';

  /*----------- Preloader -----------*/
  jQuery(window).load(function() {
    jQuery('.spinner').fadeOut();
    jQuery('.preloader').delay(1000).fadeOut('slow');
  });


  /*----------- Datepicker for forms -----------*/
  $('#date, #check-in-date, #check-out-date').datepicker();


  /*----------- Video background sections  -----------*/
  $('.header-agency-2,.video-3, .header-app-4,.video-7').vide('video/Spacious');
  $('.header-travel-1').vide('video/Boats_Maze');

  /*----------- Galleries -----------*/
  $('.gallery,.portfolio,.portfolio-masonry,.carousel-type-1, .screenshot-carousel').magnificPopup({
    delegate: 'a',
    type: 'image',
    gallery: {
      enabled: true
    }
  });

  /*----------- One Page Nav -----------*/
  $('.arpa-nav').onePageNav({
    currentClass: 'current',
    easing: 'easeInOutCubic',
    scrollThreshold: 0.2,
    filter: ':not(.external)',
    changeHash: false
  });

  /*----------- LocalScroll Internal Pages -----------*/

  $('.local-scroll').localScroll({
    duration: 2500,
    easing: 'easeInOutCubic'
  });

  /*----------- Portfolio Section -----------*/
  $('.portfolio').isotope({
    itemSelector: '.portfolio-item',
    layoutMode: 'fitRows'
  });
  $('.work-links ul li').click(function() {
    $('.work-links ul li').removeClass('active');
    $(this).addClass('active');

    var selector = $(this).attr('data-filter');
    $('.portfolio').isotope({
      filter: selector
    });
    return false;
  });
  /*----------- Portfolio Section - Masonry  -----------*/
  var $masonry = $('.portfolio-masonry').isotope({
    itemSelector: '.portfolio-item',
    percentPosition: true,
    layoutMode: 'masonry',
    masonry: {
      columnWidth: '.grid-sizer'
    }
  });
  $masonry.imagesLoaded().progress(function() {
    $masonry.isotope('layout');
  });


  /*----------- Video Lightbox -----------*/
  $('.button-video').magnificPopup({
    type: 'iframe',
    disableOn: 320
  });

  /*----------- Responsive Video -----------*/
  $('.video-container').fitVids();


  /*----------- Carousel - Multiple Item  -----------*/
  var $carousel = $('.testimonial-carousel, .screenshot-carousel, .course-carousel, .testimonial-carousel-3, .tours-carousel, .team-carousel, .property-carousel');
  $carousel.owlCarousel({
    autoplay: true,
    loop:true,
    autoplayTimeout:1000,
    items: 4,
    itemsDesktop: [1170, 4],
    itemsDesktopSmall: [991, 3],
    itemsTablet: [694, 2],
    itemsMobile: [480, 1]
  });

  /*----------- Carousel - Single Item  -----------*/
  var $testimonialTwo = $('.testimonial-carousel-1, .testimonial-carousel-2');
  $testimonialTwo.owlCarousel({
    autoplay: true,
    items: 1
  });

  /*----------- EasyTabs -----------*/
  $('.features-container,.chapter-excerpts,.event-days').easytabs({
    animationSpeed: 500,
    updateHash: false,
  });

  /*----------- Numbers Counter -----------*/
  $('.counter').counterUp({
    delay: 5,
    time: 3000
  });


  /*----------- Coming Soon  -----------*/
  /* Coming Soon - Countdown Style 1 */

  $('#countdown').countdown('2019/07/09', function(event) { //Date format 'YYYY/MM/DD'
    $(this).html(event.strftime('%D Days &amp; %H:%M:%S'));
  });

  /* Coming Soon - Countdown Style 2 */
  $('#countdown-2').countdown('2019/07/09', function(event) {
    $(this).html(event.strftime('<div class="countdown-time"><div class="counter">%D</div><div class="small">Days</div></div>' +
      '<div class="countdown-time"><div class="counter">%H</div><div class="small">Hours</div></div>' +
      '<div class="countdown-time"><div class="counter">%M</div><div class="small">Days</div></div>' +
      '<div class="countdown-time"><div class="counter">%S</div><div class="small">Seconds</div></div>'));
  });

  /*----------- Navigation Visible on scroll -----------*/

  $(window).scroll(function() {
    var scroll = $(window).scrollTop();
    if (scroll >= 90) {
      $('.scroll-dark').addClass('nav-dark-scrolled');
      $('.scroll-light').addClass('nav-light-scrolled');
    } else {
      $('.scroll-dark').removeClass('nav-dark-scrolled');
      $('.scroll-light').removeClass('nav-light-scrolled');
    }
    return false;
  });

});

/*----------  Back to top button -- Remove from download version  ----------*/
$(window).scroll(function() {
  if ($(window).scrollTop() > 360) {
    $('.back-to-top').fadeIn('slow');
  } else {
    $('.back-to-top').fadeOut('slow');
  }
});

$('a.top').click(function(e) {
  e.preventDefault();
  $('body,html').animate({
    scrollTop: 0,
  }, 1200);
});

/*==========================================
=            Malichimp Function            =
==========================================*/

$('#subscription').ajaxChimp({
  callback: mailchimpCallback,

  /* Place your URL here */
  url: 'http://paperboatdesigns.us12.list-manage.com/subscribe/post?u=d83b46829c894345bed5137e4&amp;id=ce2c39616e',

});

function mailchimpCallback(resp) {
  if (resp.result === 'success') {
    $('.subscription-success')
      .html(resp.msg)
      .fadeIn(1000);

    $('.subscription-failure').fadeOut(500);

  } else if (resp.result === 'error') {
    $('.subscription-failure')
      .html(resp.msg)
      .fadeIn(1000);

    $('.subscription-success').fadeOut(500);
  }
}

/*=====  End of Malichimp Function  ======*/

/*=============================================>>>>>
= Agency Contact Form Email =
===============================================>>>>>*/
$("#contact-form").submit(function(e) {
  e.preventDefault();
  var name = $("#name").val();
  var email = $("#email").val();
  var phone = $("#phone").val();
  var message = $("#message").val();
  var dataString = 'name=' + name + '&email=' + email + '&phone=' + phone + '&message=' + message;

  function isValidEmail(emailAddress) {
    var pattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);
    return pattern.test(emailAddress);
  }

  if (isValidEmail(email) && (message.length > 1) && (name.length > 1)) {
    $.ajax({
      type: "POST",
      url: "php/contact.php",
      data: dataString,
      success: function() {
        $('.email-success').fadeIn(1000);
        $('.email-failed').fadeOut(500);
      }
    });
  } else {
    $('.email-failed').fadeIn(1000);
    $('.email-success').fadeOut(500);
  }

  return false;
});

/*=====  End of Agency Contact Form Email  ======*/

/*================================================================
=            Restaurent & Cofeehouse Reservation Form            =
================================================================*/
$("#reservation").submit(function(e) {
  e.preventDefault();
  var name = $("#name").val();
  var email = $("#email").val();
  var phone = $("#phone").val();
  var people = $("#people").val();
  var date = $("#date").val();
  var time = $("#time").val();
  var dataString = 'name=' + name + '&email=' + email + '&phone=' + phone + '&people=' + people + '&date=' + date + '&time=' + time;

  function isValidEmail(emailAddress) {
    var pattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);
    return pattern.test(emailAddress);
  }

  if (isValidEmail(email) && (name.length > 1)) {
    $.ajax({
      type: "POST",
      url: "php/reserve.php",
      data: dataString,
      success: function() {
        $('.email-success').fadeIn(1000);
        $('.email-failed').fadeOut(500);
      }
    });
  } else {
    $('.email-failed').fadeIn(1000);
    $('.email-success').fadeOut(500);
  }

  return false;
});


/*=====  End of Restaurent & Cofeehouse Reservation Form  ======*/