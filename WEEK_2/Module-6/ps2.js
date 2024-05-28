
const frands = ["Rohim","korim","jobbarrrrrr","salam","borkot","bangladesh"];

const chackFrends = (array) =>{
    let biggestName = array[0];

    for(let i=0; i<array.length; i++){
        const element = array[i];
        if(element.length > biggestName.length){
            biggestName = element;
        }
    }
    return biggestName;
}
const bfrend = chackFrends(frands);
console.log(bfrend);