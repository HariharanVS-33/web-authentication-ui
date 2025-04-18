function togglePassword(fieldId, iconElement) {
    const passwordInput = document.getElementById(fieldId);
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        iconElement.src = "/static/eye-off.png";
    } else {
        passwordInput.type = "password";
        iconElement.src = "/static/eye.png";
    }
}
