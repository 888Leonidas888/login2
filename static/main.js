const btnLogin = document.getElementById('btn');
const email = document.getElementById('email').value;
const password = document.getElementById('password').value;

btnLogin.addEventListener('click', function (event) {
  event.preventDefault();
  const data = {
    email,
    password,
  };

  const url = 'http://127.0.0.1:5000/validate';
  fetch(url, {
    method: 'POST',
    headers: {
      'Content-type': 'application/json',
    },
    body: JSON.stringify(data),
  })
    .then((r) => {
      alert(r.url);
      window.location.href = r.url;
    })
    .catch((err) => alert(err.message));
});
