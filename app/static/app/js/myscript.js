$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: false,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: false,
        },
        1000: {
            items: 5,
            nav: true,
            loop: false,
            autoplay: false,
        }
    }
})