document.addEventListener('DOMContentLoaded', function () {
    const steps = document.querySelectorAll('.form-step');
    const nextButtons = document.querySelectorAll('.next-btn');
    const prevButtons = document.querySelectorAll('.prev-btn');

    let currentStep = 0;

    function showStep(step) {
        steps.forEach((stepElement, index) => {
            if (index === step) {
                stepElement.classList.add('active');
            } else {
                stepElement.classList.remove('active');
            }
        });
    }

    function handleKeyPress(event) {
        console.log("pressed")
        if (event.key === 'Enter') {
            event.preventDefault(); // Prevent form submission
            if (currentStep < steps.length - 1) {
                currentStep++;
                showStep(currentStep);
            }
        }
    }

    nextButtons.forEach((button, index) => {
        button.addEventListener('click', () => {
            currentStep++;
            if (currentStep < steps.length) {
                showStep(currentStep);
            }
            showStep(currentStep);
        });
    });
    prevButtons.forEach((button, index) => {
        button.addEventListener('click', () => {
            currentStep--;
            if (currentStep < 0) {
                showStep(0);
            }
            showStep(currentStep);
        });
    });
    document.getElementById('signup-form').addEventListener('keydown', handleKeyPress);
});