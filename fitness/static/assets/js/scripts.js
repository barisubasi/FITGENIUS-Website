// BMI hesaplama fonksiyonu
function calculateBMI() {
    // Formdan boy ve kilo değerlerini al
    var height = parseFloat(document.getElementById("height").value);
    var weight = parseFloat(document.getElementById("weight").value);

    // Geçerli bir sayı olup olmadığını kontrol et
    if (isNaN(height) || isNaN(weight)) {
        document.getElementById("result").innerHTML = "Lütfen geçerli bir boy ve kilo girin.";
        return;
    }

    // BMI hesaplama
    var bmi = weight / ((height / 100) * (height / 100));
    var bmiRounded = bmi.toFixed(2);

    // Sonucu oluştur
    var resultText = "Vücut Kitle Endeksi (BMI): " + bmiRounded;

    // BMI kategorisine göre ek açıklamalar ekle
    if (bmi < 18.5) {
        resultText += " (Zayıf)";
    } else if (bmi < 24.9) {
        resultText += " (Normal)";
    } else if (bmi < 29.9) {
        resultText += " (Fazla Kilolu)";
    } else {
        resultText += " (Obez)";
    }

    // Sonucu göster
    document.getElementById("result").innerHTML = resultText;
}

// Giriş veya kayıt formunu gösterme fonksiyonu
function showForm(formId, button) {
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

// Şifre eşleşme kontrolü fonksiyonu
function validatePassword() {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirmPassword").value;
    // Şifrelerin eşleşip eşleşmediğini kontrol et
    if (password !== confirmPassword) {
        alert("Şifreler eşleşmiyor. Lütfen tekrar kontrol edin.");
        return false;
    }
    alert("Kayıt başarıyla tamamlandı!"); // Başarılı kayıt mesajı
}
