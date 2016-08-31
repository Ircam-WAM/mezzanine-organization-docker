var LightSliderHomeInit = function() {

    //
    // Init
    //
    this.init();

};

LightSliderHomeInit.prototype.init = function() {

    var that = this;

    $('[data-slider-home]').lightSlider({
        item: 1,
        slideMargin: 0,
        pager: false,
        loop: true,
        onAfterSlide: function(slider) {
            var $pages = slider.parents('.slider-home').find('.slider-home__pager li');
            $pages.removeClass('active');
            console.log(slider.getCurrentSlideCount());
            $($pages[slider.getCurrentSlideCount()-1]).addClass('active');
        },
        onSliderLoad: function(slider) {
            var $pages = slider.parents('.slider-home').find('.slider-home__pager li');
            $pages.each(function(idx) {
                var that = $(this);
                that.click(function(e) {
                    e.preventDefault();
                    $pages.removeClass('active');
                    that.addClass('active');
                    slider.goToSlide(idx);
                    return false;
                });

            });
        }
    });

};

module.exports = LightSliderHomeInit;