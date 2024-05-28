

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

const res = product.forEach(product =>{
    console.log(product.id);  
});
console.log(res);