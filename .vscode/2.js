
// let a = document.querySelector("h1");
// a.addEventListener("dblclick", function(){
//     a.style.color = "red";
// })

// let b = document.querySelector("input");
// b.addEventListener("input", zozo);
// function zozo(chr){
//     b.style.backgroundColor = "green";
//     if (chr.data !== null){
//         console.log(chr.data);
//     }
// }
// -- way 2 // let b = document.querySelector("input");
// b.addEventListener("input",function (chr){
//     b.style.backgroundColor = "green";
//     if (chr.data !== null){
//         console.log(chr.data);
//     }} );

// pj-5 -----------------------
// let a = document.querySelector("select");
// let tchg = document.querySelector("#cng");
// a.addEventListener("change", function(dat){
//     // h1.style.text-transform :capitalize;
//     tchg.textContent = `${dat.target.value} seleted` //for on show not namem like apple is seled "ok seled"
//     console.log(dat.target.value);
// });

// pj-6----------------
// let h = document.querySelector("h1");
// window.addEventListener("keydown", function (inp){
//  if (inp.key === " " ){
//     h.textContent = "SPC";
//  } else {
//     h.textContent = inp.key; 
//  }
// });

// pj-7
// let btn = document.querySelector("#btn");
// let fileinp = document.querySelector("#fileinp");
// btn.addEventListener("click", function (){
// fileinp.click();
// });
// fileinp.addEventListener("change", function (files) {
//     const file = files.target.files[0];
//     if (file) {
//        btn.textContent = file.name; 
//     }
// });

// Solution
// let time = 12;
// let cnt = setInterval( () =>{
//            if (time >= 0) {
//             console.log(time);
//             time--;
//         } else 
//             clearTimeout(cnt)
//         },1000)