

const product = [
    {
        id: 1,
        name: "Xiaomi",
        description: "this is Xiaomi",
        price: `$644`,
        color: "black"
    },

    {
        id: 2,
        name: "samsung",
        description: "this is samsung",
        price: `$644`,
        color: "red"
    },

    {
        id: 3,
        name: "iphone",
        description: "this is iphone",
        price: `$644`,
        color: "blue"
    },

    {
        id: 4,
        name: "walton",
        description: "this is walton",
        price: `$644`,
        color: "black"
    },
]

// for (let i = 0; i < product.length; i++) {
//     const elements = product[i];
//     if (elements.id == 3) {
//         console.log(elements);
//     }
// }

// const res = product.find(pd => pd.id == 2);
// console.log(res);


const res = product.filter(product=>product.color == "blacks");
console.log(res);