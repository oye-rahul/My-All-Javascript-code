// let a = 10;
// let b = 20;
// let c = a+b;
// console.log(c);

// function add(v1,v2){
//     return v1 + v2;
// }
// console.log(add(15,25))

// for(let i = 1; i <11; i++){
//     console.log(i);
// }

// function add(v1,v2){
//     return v1 * v2;
// }
// console.log(add(5,6))

// function chk (v1){
//     if(v1%2 === 0)
//         return "true number is even";
//     if(v1%2 === 1)
//         return "false number is odd";
// }
// console.log(chk(4));
// console.log(chk(7));

// function isEven(v1) {
//     return v1 % 2 === 0;
// }
// console.log(isEven(4)); 
// console.log(isEven(7)); 

// function name (v1="guest"){
//     return "hay, " + v1;
// }
// console.log(name("rahul"));
// console.log(name());

// let multy = (a,b) => {
//      return a * b;
// };
// console.log(multy(5,6));

// function num (n){
//     for(let i = 1; i<=n; i++)
//         console.log(i)
// }
// num (5)

// function test (v1){
//     if(v1 < 0) return "Negative";
//     if(v1 === 0) return "equl";
//     if(v1 > 0)return "Positive";
// }
// console.log(test(10))
// console.log(test(-5))
// console.log(test(0))

// function sqr (v1){
//     return (v1*v1)
// }

// console.log(sqr(7))

// function big (v1,v2){
//     if(v1 < v2) return v2;
//     return v1;
// }
// console.log(big(50,30))


// function sumN(n) {
//     let total = 0;
//     for (let i = 1; i <= n; i++) {
//         total += i; // add i to total
//     }
//     return total;
// }

// console.log(sumN(10)); // 55
// abcd();

// (function (){
//     console.log("hey");
// })();

// function abcd(){
//     console.log("helo");
// }

// function dsc (discount){
//     return function (price){
//         return price - price * (discount / 100);
//     };
// }

// let dsc_ten = dsc(10);
// let dsc_twenty = dsc(20);

// console.log(dsc_ten(1999).toFixed(0));
// console.log(dsc_twenty(799));
//  let arr = [1,2,3,4,5];
// console.log(arr)

//  let newarr = arr.slice(0,3);
// console.log(newarr)

// let obj = {
//     name : "rahul",
//     age : 20,
// };
// let aa = "name";


// function a (num){
//     if(num > 0)return "Positive";
//     else if(num < 0)return "Negative";
//     else return "Zero"
// }
// console.log(a(-2))

// function line(n){
//  for (let i = 1; i <= n; i++){
//     console.log(i);
// }
// }
// line(10)

// function total (num){
//     let total = 0;
//     for (let i = 0;i < num.length; i++){
//         total += num[i];
//     }
//     return total;
// }
// console.log(total([2,3,5,8,9,]))

//-----------------------------------------------

// let a = 42;
// a = 55;
// console.log(a);

// function x (){
//     let a = 10;
//     let b = 1;
//     if (a === b) {
//         return "match"
//     } else {
//         return "not match"
//     }
// }
// console.log(x());
// condition ? valueIfTrue : valueIfFalse
// function xx (){
//     let a = 10;
//     let b = 1;
//     let y =  a === b ? "ok match" : "not match" ;
//     return y;
// }
// console.log(xx());

// let mark = 89;
// function grade(mark){
// if (mark > 101 ||  mark < 0) {
//     return "invelid";
// } else if (mark >= 90) {
//      return "A";
// } else if (mark >= 80){
//      return "b";
// } else {
//    return "c";
// }
// }
// console.log(grade(95));

// function chk (age){
//     if (age < 18){
// return "not alw";
//     } else if (age > 18){
// return "alw";
//     }
//     return "enter age";
// };
// console.log(chk())

// function mark (val){
//     if (val > 100){
//         return "invelid";
//     } else if (val >= 90){
//         return "grd is 'A' mark is = " + val;
//     } else if (val >= 80){
//         return "b";
//     } else if (val >= 70){
//         return "c";
//     } else if (val >= 60){
//         return "d";
//     } else if (val >= 50){
//         return "e";
//     } else {
//         return "fail";
//     }
// }
// console.log(mark(98));

// function game(user1, user2){
//     if(user1 === user2) return "draw";
//     if(user1 === "rock" && user2 === "scir") return "1 win";
//     if(user1 === "sicr" && user2 === "paper") return "1 win";
//     if(user1 === "paper" && user2 === "rock") return "1 win";
//     return "2 win";
// }
// console.log(game("paper", "scir"));

// function which_cloth (weather){
//     // let weather = "normal";
//     switch (weather) {
//         case "rainy":
//             console.log("u want to wer rain kot");
//             break;
//         case "sunny":
//             console.log("u want to wer shirt");
//             break;
//         case "wintter":
//             console.log("u want to wer swt");
//             break;
//         case "normal":
//             console.log("want to wer hodi");
//             break;
//         default:
//             console.log("enter valied");
//             break;
//     }
// }
// which_cloth("normal")
