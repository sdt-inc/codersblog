function sayHello(who) {
    document.write("Hello, " + who);
}

function alarm() {
    alert("Django static file testing!");
}


function progressIndicator(window, document) {
    const progressIndicatorForElement = document.querySelector('[data-progress-indicator]');
    if (!progressIndicatorForElement) {
        return;
    }

    const progressElement = document.createElement('div');
    progressElement.setAttribute('role', 'presentation');
    progressElement.classList.add('progress-indicator');

    // Initial position.
    progressElement.style.left = "-100%";
    progressElement.style.transform = "translateX(-100%)";

    document.body.appendChild(progressElement);

    let lastKnownScrollPosition = 0;
    let ticking = false;

    window.addEventListener('scroll', function(e) {
        lastKnownScrollPosition = window.scrollY;
        if (ticking) {
            return;
        }
        window.requestAnimationFrame(function() {
            var offset = Math.min(100, lastKnownScrollPosition / (progressIndicatorForElement.scrollHeight - window.innerHeight) * 100);
            progressElement.style.transform = `translateX(${offset}%)`;
            ticking = false;
        });
        ticking = true;
    });
}