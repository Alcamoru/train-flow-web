let currentStep = 0;
const steps = document.querySelectorAll(".athlete-form-step");
const titles = document.querySelectorAll(".signup-step");

document.addEventListener("DOMContentLoaded", () => {
    showStep(currentStep);
});

function showStep(step) {
    steps.forEach((s, index) => {
        if (index === currentStep) {
            s.classList.add('active');
        }
        else {
            s.classList.remove('active');
        }
    });
    titles.forEach((title, index) => {
        title.classList.remove("active-step")
    })
    titles.forEach((title, index) => {
        if (index === currentStep) {
            title.classList.add("active-step");
        }
    })
}

function nextStep() {
    if (currentStep < steps.length - 1) {
        currentStep++;
        showStep(currentStep);
    }
}

function prevStep() {
    if (currentStep > 0) {
        currentStep--;
        showStep(currentStep);
    }
}