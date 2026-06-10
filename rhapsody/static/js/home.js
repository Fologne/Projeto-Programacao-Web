const slides = document.querySelectorAll('.slide');
const dots = document.querySelectorAll('.dot');

let current = 0;

function showSlide(index){
    slides.forEach(slide =>
        slide.classList.remove('active')
    );
    dots.forEach(dot =>
        dot.classList.remove('active-dot')
    );
    slides[index].classList.add('active');
    dots[index].classList.add('active-dot');
    current = index;
}

document.querySelector('.next').addEventListener('click', () => {
    let next = current + 1;
    if(next >= slides.length){
        next = 0;
    }
    showSlide(next);
});

document.querySelector('.prev').addEventListener('click', () => {
    let prev = current - 1;
    if(prev < 0){
        prev = slides.length - 1;
    }
    showSlide(prev);
});

setInterval(() => {
    let next = current + 1;
    if(next >= slides.length){
        next = 0;
    }
    showSlide(next);
}, 5000);