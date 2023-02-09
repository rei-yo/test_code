// const greeting = document.querySelectorAll('.animation');

// greeting.forEach(sentence => {
//     let split_char = sentence.innerHTML.trim().split('');
//     console.log(split_char);
//     sentence.innerHTML = split_char.reduce((accu, curr) => {
//         curr = curr.replace(' ', '&nbsp;')
//         return `${accu}<span class= 'char'>${curr}</span>`
//     },'');
// });

// const cb = function(all_sentence, observer) {
//     all_sentence.forEach(sentence => {
//         if(sentence.isIntersecting) {
//             console.log(sentence.target);
//             // sentence.classList.toggle('active');
//         }else{
//             console.log('out');
//         }
//     })
// }

class ActiveOnOff{
    constructor(el) {
        this.el = el;
        this.chars = this.el.innerHTML.trim().split('');
        this.el.innerHTML = this._spanTag();
    }
    _spanTag(){
        return this.chars.reduce((accu, curr) => {
                    curr = curr.replace(' ', '&nbsp;');
                    return `${accu}<span class= 'char'>${curr}</span>`;
        },'');
    };

    activeOn(){
        this.el.classList.toggle('active');
    }

}