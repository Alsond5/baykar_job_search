window.onload = function() {
    const goTop = document.querySelector('.goTop');
    const showOn = 100;

    const scroll = () => {
        return document.documentElement || document.body;
    };

    document.addEventListener("scroll", () => {
        if (scroll().scrollTop > showOn) {
            goTop.classList.add('active');
        }
        else {
            goTop.classList.remove('active');
        }
    });

    const goToTop = () => {
        document.body.scrollIntoView({
            behavior: 'smooth',
        });
    };

    goTop.addEventListener("click", goToTop);
}