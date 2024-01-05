// 基础的语法




document.write('hello js');
console.log("hello js");
const cars = ["Tesla", "Volvo", "BMW"];
document.write(cars.length)
for (let index = 0; index <cars.length; index++) {
    const element = cars[index];
    console.log(element)
    
}
// array.forEach(element => {
    // 常常当作循环的语句怼我们的数据进行遍历的操作
// });
cars.forEach((e)=>{
    console.log(e)
})
cars.push("杰克","BWM");
cars.forEach((E)=>{
    console.log(E)
})