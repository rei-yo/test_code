// document.addEventListener('DOMContentLoaded', function() {
//     const greet = document.querySelectorAll('.animation');
//     cb = function(entries, obsever) {
//         entries.forEach(entry => {
//             if(entry.isIntersectin)
//         })
//     }
// })

const all_sentence = document.querySelectorAll('.animation');
const cb = function(entries, observer) {
    entries.forEach(entry => {
        if(entry.isIntersecting) {
            console.log(entry.target);
            const ta = new ActiveOnOff(entry.target);
            ta.activeOn();
            console.log(observer);
            observer.unobserve(entry.target);
        }else{
            console.log('out');
        }
    })
}
const io = new IntersectionObserver(cb);
all_sentence.forEach(sentence => {io.observe(sentence);});
