(function () {
  const loginRadio  = document.getElementById('login');
  const signupRadio = document.getElementById('signup');
  const formInner   = document.querySelector('.form-inner');

  const loginLabel  = document.querySelector('label.login');
  const signupLabel = document.querySelector('label.signup');
  const signupLink  = document.querySelector('form.login .signup-link a');

  function showLogin() {
    loginRadio.checked = true;             // таб бегает по твоему CSS
    formInner.style.marginLeft = '0%';     // сдвигаем контейнер форм
  }
  function showSignup() {
    signupRadio.checked = true;
    formInner.style.marginLeft = '-50%';
  }

  // клики по табам
  if (loginLabel)  loginLabel.addEventListener('click', showLogin);
  if (signupLabel) signupLabel.addEventListener('click', showSignup);

  // ссылка "Signup now"
  if (signupLink) {
    signupLink.addEventListener('click', function (e) {
      e.preventDefault();
      showSignup();
    });
  }

  // начальное состояние
  if (signupRadio && signupRadio.checked) showSignup();
  else showLogin();
})();
