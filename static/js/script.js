const passwordInput = document.getElementById('password');
        const strengthMeter = document.getElementById('strengthMeter');
        const generatePasswordBtn = document.getElementById('generatePassword');

        passwordInput.addEventListener('input', function() {
            updateStrengthMeter(passwordInput.value);
        });

        generatePasswordBtn.addEventListener('click', function() {
            const strongPassword = generateStrongPassword();
            passwordInput.value = strongPassword;
            updateStrengthMeter(strongPassword);
        });

        function updateStrengthMeter(val) {
            const meter = strengthMeter.children;

            let strength = 0;
            if (val.length >= 8) {
                strength += 1;
            }
            if (/[A-Z]/.test(val)) {
                strength += 1;
            }
            if (/[0-9]/.test(val)) {
                strength += 1;
            }
            if (/[^A-Za-z0-9]/.test(val)) {
                strength += 1;
            }
            if (val.length >= 12) {
                strength += 1; // Additional strength for passwords longer than 12 characters
            }

            for (let i = 0; i < meter.length; i++) {
                meter[i].className = '';
                if (strength > i) {
                    if (strength === 1) {
                        meter[i].classList.add('weak');
                    } else if (strength === 2) {
                        meter[i].classList.add('medium');
                    } else if (strength === 3) {
                        meter[i].classList.add('strong');
                    } else if (strength > 3) {
                        meter[i].classList.add('very-strong');
                    }
                }
            }
        }

        function generateStrongPassword() {
            const length = 16; // Desired length of the strong password
            const charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+~`|}{[]:;?><,./-=';
            let password = '';
            for (let i = 0; i < length; i++) {
                const randomIndex = Math.floor(Math.random() * charset.length);
                password += charset[randomIndex];
            }
            return password;
        }



        document.getElementById('menubtn').addEventListener('click', function(){
            var header = document.getElementById('header');
            header.classList.toggle('show');
        })