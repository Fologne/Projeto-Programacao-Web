const input = document.getElementById("imagemInput");
const preview = document.getElementById("preview");

input.addEventListener("change", function(){
    const file = this.files[0];
    if(file){
        preview.src = URL.createObjectURL(file);
    }
});