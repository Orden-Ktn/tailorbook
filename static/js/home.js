// Add smooth scroll behavior
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Add parallax effect to background pattern
let scrollY = 0;
window.addEventListener('scroll', () => {
    scrollY = window.scrollY;
    document.querySelector('.background-pattern').style.transform = 
        `translate(${scrollY * 0.05}px, ${scrollY * 0.05}px)`;
});