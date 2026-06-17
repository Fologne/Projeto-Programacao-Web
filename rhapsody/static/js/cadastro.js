const produtoForm = document.getElementById("produtoForm");
if (produtoForm) {
    produtoForm.addEventListener("submit", function(e) {
        const preco = document.querySelector("input[name='preco']").value;
        const estoque = document.querySelector("input[name='estoque']").value;

        if (preco <= 0) {
            alert("O preço deve ser maior que 0");
            e.preventDefault();
        }

        if (estoque < 0) {
            alert("Estoque não pode ser negativo");
            e.preventDefault();
        }
    });
}
window.addEventListener("load", function () {
    const popup = document.querySelector('.popup');

    if (popup) {
        setTimeout(() => {
            popup.style.opacity = '0';
            popup.style.transition = '0.5s';

            setTimeout(() => {
                popup.remove();
            }, 500);
        }, 3000);
    }
});