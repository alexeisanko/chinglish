$('.rewievs__slider').owlCarousel({
    loop: true,
    margin: 20,
    nav: true,
    dots: false,
    responsive: {
        0: {
            items: 1,
            dots: true,
            nav: false
        },
        600: {
            items: 1,
            dots: true,
            nav: false
        },
        1000: {
            items: 2
        }
    }
});
$('.cert').owlCarousel({
    loop: true,
    margin: 20,
    nav: true,
    dots: false,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 2
        },
        1000: {
            items: 3

        }
    }
})
