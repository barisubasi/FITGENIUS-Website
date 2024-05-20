function calculateBMI() {
    var height = parseFloat(document.getElementById("height").value);
    var weight = parseFloat(document.getElementById("weight").value);

    if (isNaN(height) || isNaN(weight)) {
        document.getElementById("result").innerHTML = "Lütfen geçerli bir boy ve kilo girin.";
        return;
    }

    var bmi = weight / ((height / 100) * (height / 100));
    var bmiRounded = bmi.toFixed(2);

    var resultText = "Vücut Kitle Endeksi (BMI): " + bmiRounded;

    if (bmi < 18.5) {
        resultText += " (Zayıf)";
    } else if (bmi < 24.9) {
        resultText += " (Normal)";
    } else if (bmi < 29.9) {
        resultText += " (Fazla Kilolu)";
    } else {
        resultText += " (Obez)";
    }

    document.getElementById("result").innerHTML = resultText;
}

function showForm(formId,button) {
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');
    if (formId === 'loginForm') {
    loginForm.style.display = 'block';
    registerForm.style.display = 'none';
    button.classList.add('active');
    document.querySelector('.register-choice-button').classList.remove('active');
    } else if (formId === 'registerForm') {
    loginForm.style.display = 'none';
    registerForm.style.display = 'block';
    button.classList.add('active');
    document.querySelector('.login-choice-button').classList.remove('active');
    }
    }
    function validatePassword() {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirmPassword").value;
    if (password !== confirmPassword) {
    alert("Şifreler eşleşmiyor. Lütfen tekrar kontrol edin.");
    return false;
    }
    alert("Kayıt başarıyla tamamlandı!");
    }
    