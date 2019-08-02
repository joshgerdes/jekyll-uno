---
    layout: null
    sitemap:
        exclude: 'yes'
---


    $(document).ready(function () {
      $('.btn-mobile-menu').unbind('click').click(function (e) {
        $('.navigation-wrapper').toggleClass('visible animated bounceInDown');
        $('.btn-mobile-menu__icon').toggleClass('icon-list icon-x-circle animated fadeIn');
      });


      if (window.location.hash && window.location.hash === '#blog') {
        $('.panel-cover').addClass('panel-cover--collapsed');
        $('.content-wrapper.blog').removeClass('hidden').addClass('visible');
        $('a.about-button').removeClass('active');
        $('a.blog-button').addClass('active');
      }
      if (window.location.hash && window.location.hash === '#about-me') {
        $('.panel-cover').addClass('panel-cover--collapsed right');
        $('.content-wrapper.about').removeClass('hidden').addClass('visible');
        $('a.blog-button').removeClass('active');
        $('a.about-button').addClass('active');
      }

      if (window.location.pathname !== '{{ site.baseurl }}/' && window.location.pathname !== '{{ site.baseurl }}/index.html'
          && window.location.hash !== '#about-me') {
        $('.panel-cover').addClass('panel-cover--collapsed');
        $('.content-wrapper.blog').removeClass('hidden').addClass('visible');
        $('a.about-button').removeClass('active');
        $('a.blog-button').addClass('active');
      }

      $('a.blog-button').click(function (e) {
        // Case where the panel is already opened
        if ($('.panel-cover').hasClass('panel-cover--collapsed')) {
          if ($('.panel-cover').hasClass('right')) {
            // Case where the about section is opened
            $('.content-wrapper.about').removeClass('visible animated slideInLeft').addClass('hidden');
            $('.panel-cover').animate({'right' : '', 'left' : '0'}, 400, swing = 'swing', function () {
              $('.panel-cover').removeClass('right').removeAttr('style');
              $('a.about-button').removeClass('active');
              $('a.blog-button').addClass('active');
              $('.content-wrapper.blog').removeClass('hidden').addClass('visible animated slideInRight');

            })
          }
          return;
        }
        // Test for the size of the window
        let currentWidth = $('.panel-cover').width();
        if (currentWidth < 900) {
          // Mean mobile phone
          $('.panel-cover').addClass('panel-cover--collapsed');
          $('.content-wrapper').addClass('animated slideInRight');
        }
        else {
          // Mean desktop
          $('.panel-cover').css('max-width', currentWidth);
          $('.panel-cover').animate({'max-width': '530px', 'width': '40%'}, 400, swing = 'swing', function () {
            $('.panel-cover').addClass('panel-cover--collapsed').removeAttr('style');
            $('a.about-button').removeClass('active');
            $('a.blog-button').addClass('active');
            $('.content-wrapper.blog').removeClass('hidden').addClass('visible animated slideInRight');
          })
        }
      });

      $('a.about-button').click(function (e) {
        // Case where the panel is already opened
        if ($('.panel-cover').hasClass('panel-cover--collapsed')) {
          // Case where the about section is opened
          if (! $('.panel-cover').hasClass('right')) {
            $('.content-wrapper.blog').removeClass('visible animated slideInRight').addClass('hidden');
            $('.panel-cover').animate({'right' : '0'}, 400, swing = 'swing', function () {
              $('.panel-cover').addClass('right').removeAttr('style');
              $('a.blog-button').removeClass('active');
              $('a.about-button').addClass('active');
              $('.content-wrapper.about').removeClass('hidden').addClass('visible animated slideInLeft');

            })
          }
          return;
        }
        // Test for the size of the window
        let currentWidth = $('.panel-cover').width();
        if (currentWidth < 900) {
          // Mean mobile phone
          $('.panel-cover').addClass('panel-cover--collapsed');
          $('.content-wrapper').addClass('animated slideInLeft');
        }
        else {
          // Mean desktop
          $('.panel-cover').css('max-width', currentWidth);
          $('.panel-cover').animate({'max-width': '530px', 'width': '40%', 'right' : '0'}, 400, swing = 'swing', function () {
            $('.panel-cover').addClass('panel-cover--collapsed right').removeAttr('style');
            $('a.blog-button').removeClass('active');
            $('a.about-button').addClass('active');
            $('.content-wrapper.about').removeClass('hidden').addClass('visible animated slideInLeft');

          })
        }
      });

    });