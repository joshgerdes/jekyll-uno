---
layout: null
---
$(document).ready(function () {
  // blog button click
  $('a.blog-button').click(function (e) {
    if ($('.panel-cover').hasClass('panel-cover--collapsed')) {
      $('.content-wrapper').addClass('animated slideOutRight')
      width = $(window).width()
      $('.panel-cover').animate({'max-width': width + 'px', 'width': '100%'}, 400, swing = 'swing', function () {
        window.location.replace('/')
      })
      $('.panel-cover').removeClass('panel-cover--collapsed')
    } else {
      currentWidth = $('.panel-cover').width()
      if (currentWidth < 960) {
        $('.content-wrapper').addClass('animated slideInRight')
        $('.btn-mobile-menu__icon').toggleClass('icon-list icon-x-circle animated fadeOut')
      } else {
        $('.panel-cover').css('max-width', currentWidth)
        $('.panel-cover').animate({'max-width': '530px', 'width': '40%'}, 400, swing = 'swing', function () {})
      }
      $('.panel-cover').addClass('panel-cover--collapsed')
    }
  })

  // direct hashing to the blogs screen
  if (window.location.hash && window.location.hash == '#blogs') {
    $('.panel-cover').addClass('panel-cover--collapsed')
  }

  // default to home path
  if (window.location.pathname !== '{{ site.baseurl }}' && window.location.pathname !== '{{ site.baseurl }}index.html') {
    window.location.replace('/')
  }

  $('.btn-mobile-menu').click(function () {
    $('.navigation-wrapper').toggleClass('visible animated bounceInDown')
    $('.btn-mobile-menu__icon').toggleClass('icon-list icon-x-circle animated fadeIn')
  })

  $('.navigation-wrapper .blog-button').click(function () {
    $('.navigation-wrapper').toggleClass('visible')
    $('.btn-mobile-menu__icon').toggleClass('icon-list icon-x-circle animated fadeIn')
  })

})
