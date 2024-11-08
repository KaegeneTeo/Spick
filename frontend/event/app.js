const steps = document.querySelectorAll(".stp");
const circleSteps = document.querySelectorAll(".step");
let currentStep = 1;
let currentCircle = 0;

steps.forEach((step) => {
    const nextBtn = step.querySelector(".next-stp");
    const prevBtn = step.querySelector(".prev-stp");
  
    if (prevBtn) {
        prevBtn.addEventListener("click", () => {
            document.querySelector(`.step-${currentStep}`).style.display = "none";
            circleSteps[currentCircle].classList.remove("active");
            currentCircle--; // Move back to previous circle step
            currentStep--;
            document.querySelector(`.step-${currentStep}`).style.display = "flex";
            circleSteps[currentCircle].classList.add("active"); // Make previous circle step active
        });
    }
  
    nextBtn.addEventListener("click", () => {
        document.querySelector(`.step-${currentStep}`).style.display = "none";
        if (currentStep < 4) {
            currentStep++;
            currentCircle++;
        }
        document.querySelector(`.step-${currentStep}`).style.display = "flex";
        circleSteps[currentCircle].classList.add("active");
    });
});
