document.getElementById("signupForm").addEventListener("submit", function(e) {

    const senha = document.querySelector(
        "input[name='senha']"
    ).value;

    const confirmar = document.querySelector(
        "input[name='confirmar_senha']"
    ).value;

    if (senha !== confirmar) {

        alert("As senhas não coincidem.");

        e.preventDefault();

        return;
    }

    if (senha.length < 6) {

        alert(
            "A senha deve possuir pelo menos 6 caracteres."
        );

        e.preventDefault();
    }

});