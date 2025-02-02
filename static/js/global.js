document.addEventListener("DOMContentLoaded",function(){
    const menuToggle = document.getElementById("menu-toggle");
    const navigationBar = document.getElementById("nav_div");
    const bannerBar = document.getElementById("logo_div");

    menuToggle.addEventListener("click", function(){
        navigationBar.classList.toggle("nav_open");
        bannerBar.classList.toggle("nav_open");
    })
})