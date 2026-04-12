/** 
 * NDoubleD Portfolio Site Scripts
 * Senior Refactor: Cleaned up redundant code and improved initialization flow.
 */
"use strict";

const PortfolioSite = {
    init() {
        this.initNavigation();
        this.initPlugins();
        this.initPreloader();
    },

    initNavigation() {
        const $navMobile = $("#nav-mobile");
        const $navMain = $("#nav-main");
        const $navTrigger = $("#nav-trigger span");

        $navMobile.html($navMain.html());

        $navTrigger.on("click", () => {
            const isExpanded = $navMobile.find("ul").hasClass("expanded");
            if (isExpanded) {
                $navMobile.find("ul").removeClass("expanded").slideUp(250);
                $navTrigger.removeClass("open");
            } else {
                $navMobile.find("ul").addClass("expanded").slideDown(250);
                $navTrigger.addClass("open");
            }
        });

        // Close mobile nav on link click
        $navMobile.on("click", "a", () => {
            $navMobile.find("ul").removeClass("expanded").slideUp(250);
            $navTrigger.removeClass("open");
        });

        // Sticky Nav logic
        if ($.prototype.waypoints) {
            $('#content').waypoint((direction) => {
                $('#header').toggleClass('nav-solid fadeInDown', direction === 'down');
            });
        }
    },

    initPlugins() {
        if ($.prototype.scrollUp) $.scrollUp();
        if ($.prototype.enllax) $(window).enllax();
        if (typeof WOW === 'function') new WOW().init();
    },

    initPreloader() {
        const hidePreloader = () => {
            $('#status').fadeOut();
            $('#preloader').delay(350).fadeOut('slow');
            $('body').delay(350).css({'overflow-y': 'visible'});
        };

        $(window).on('load', hidePreloader);

        // Fail-safe: Hide preloader after 3 seconds no matter what
        setTimeout(hidePreloader, 3000);
    }
};

$(document).ready(() => PortfolioSite.init());
