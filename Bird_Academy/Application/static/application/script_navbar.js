console.log("yes!!!!!")
const menuHamburger = document.querySelector(".menu-hamburger")
const navLinks = document.querySelector(".nav-links")

menuHamburger.addEventListener('click',()=>{
navLinks.classList.toggle('mobile-menu')
})

const menuLinks = document.querySelectorAll('.nav-links ul li');

menuLinks.forEach(link => {
    link.addEventListener('click', () => {
        // Fermer le menu en retirant la classe 'mobile-menu'
        navLinks.classList.remove('mobile-menu');
    });
});