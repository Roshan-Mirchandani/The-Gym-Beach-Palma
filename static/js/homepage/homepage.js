document.addEventListener("DOMContentLoaded", function () {
  let currentIndex = 0;
  const images = document.querySelectorAll(".slider-image");

  function showSlide(index) {
    if (index >= images.length) {
      currentIndex = 0;
    } else if (index < 0) {
      currentIndex = images.length - 1;
    } else {
      currentIndex = index;
    }
  }

  images.forEach((img) => img.classList.remove("active"));

  images[currentIndex].classList.add("active");

  function moveSlide(step) {
    showSlide(currentIndex + step); // Step can be +1 for next or -1 for previous
    images.forEach((img) => img.classList.remove("active"));
    images[currentIndex].classList.add("active");
  }

  showSlide(currentIndex);

  const prevButton = document.querySelector("#prev");
  const nextButton = document.querySelector("#next");

  if (prevButton) {
    prevButton.addEventListener("click", function () {
      moveSlide(-1); // Move to previous slide
      console.log("p", currentIndex);
    });
  }

  if (nextButton) {
    nextButton.addEventListener("click", function () {
      moveSlide(1); // Move to next slide
      console.log("n", currentIndex);
    });
  }
});
