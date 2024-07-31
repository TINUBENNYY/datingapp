document.addEventListener('DOMContentLoaded', function () {
    const dropdownToggle = document.querySelector('.dropdown-toggle');
    const dropdownMenu = document.querySelector('.dropdown-menu');
    let timeout;

    dropdownToggle.addEventListener('mouseenter', function () {
        clearTimeout(timeout);
        dropdownMenu.style.display = 'block';
    });

    dropdownToggle.addEventListener('mouseleave', function () {
        timeout = setTimeout(function () {
            if (!dropdownMenu.matches(':hover')) {
                dropdownMenu.style.display = 'none';
            }
        }, 200);
    });

    dropdownMenu.addEventListener('mouseenter', function () {
        clearTimeout(timeout);
        dropdownMenu.style.display = 'block';
    });

    dropdownMenu.addEventListener('mouseleave', function () {
        dropdownMenu.style.display = 'none';
    });
});

// Hamburger menu toggle for mobile
document.querySelector('.hamburger').addEventListener('click', function() {
    this.classList.toggle('active');
    document.querySelector('.nav-menu').classList.toggle('active');
});

window.addEventListener('scroll', function() {
    var navbar = document.getElementById('navbar');
    if (window.scrollY > 50) { // Change '50' to the scroll position where the change should happen
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});
