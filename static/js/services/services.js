document.addEventListener("DOMContentLoaded", () => {
  const equipmentSlider = document.getElementById("equipment_slider");
  const equipmentImages = equipmentSlider.querySelectorAll(".slider_container img");
  const equipmentDescription = equipmentSlider.querySelector("#image_description1 p");
  let currentEquipmentIndex = 0;

  function updateEquipmentSlider(index) {
    equipmentImages.forEach((img, i) => {
      img.classList.toggle("active", i === index);
    });
    equipmentDescription.textContent = equipmentImages[index].dataset.description;
  }

  document.getElementById("next1").addEventListener("click", () => {
    currentEquipmentIndex = (currentEquipmentIndex + 1) % equipmentImages.length;
    updateEquipmentSlider(currentEquipmentIndex);
  });

  document.getElementById("prev1").addEventListener("click", () => {
    currentEquipmentIndex = (currentEquipmentIndex - 1 + equipmentImages.length) % equipmentImages.length;
    updateEquipmentSlider(currentEquipmentIndex);
  });

  const personalTrainerSlider = document.getElementById("pt_slider");
  const ptImages = personalTrainerSlider.querySelectorAll(".slider_container img");
  const ptDescription = personalTrainerSlider.querySelector("#image_description2 p");
  let currentPtIndex = 0;

  function updatePtSlider(index) {
    ptImages.forEach((img, i) => {
      img.classList.toggle("active", i === index);
    });
    ptDescription.textContent = ptImages[index].dataset.description;
  }

  document.getElementById("next2").addEventListener("click", () => {
    currentPtIndex = (currentPtIndex + 1) % ptImages.length;
    updatePtSlider(currentPtIndex);
  });

  document.getElementById("prev2").addEventListener("click", () => {
    currentPtIndex = (currentPtIndex - 1) % ptImages.length;
    updatePtSlider(currentPtIndex);
  });
});
