document.addEventListener("DOMContentLoaded", function() {
		if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
		document.body.classList.add('dark');
	}
});

function toggleNavbar() {
    var nav = document.getElementById("mobile-menu");
    nav.classList.toggle("hidden");
}

window.addEventListener('scroll', function() {
    var backToTopButton = document.getElementById('back-to-top');
    if (window.scrollY > 200) {
        backToTopButton.style.display = 'block';
    } else {
        backToTopButton.style.display = 'none';
    }
});