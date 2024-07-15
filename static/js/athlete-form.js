let currentStep = 0;
const steps = document.querySelectorAll(".athlete-form-step");

document.addEventListener("DOMContentLoaded", () => {
    showStep(currentStep);
});

function showStep(step) {
    steps.forEach((s, index) => {
        s.style.display = index === step ? "block" : "none";
    });
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