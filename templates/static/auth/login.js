function closealerta(n) {
  if (n == 1) {
    alerta = document.querySelector(".alert-red");
  } else {
        alerta = document.querySelector(".alert-succes");
  }

  alerta.style.display = "none";
  console.log(alerta);
}
