document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("quiz-form");

    form.addEventListener("submit", function (event) {
        let allAnswered = true;
        const fieldsets = form.querySelectorAll("fieldset");

        fieldsets.forEach((fieldset) => {
            const inputs = fieldset.querySelectorAll("input[type='radio']");
            const checked = Array.from(inputs).some(input => input.checked);
            if (!checked) {
                allAnswered = false;
            }
        });

        if (!allAnswered) {
            event.preventDefault();
            alert("Please answer all questions before submitting!");
        }
    });
});