
//API-> Application Programming Interface

const loadAllProduct = () => {
    fetch('https://fakestoreapi.com/products')
        .then(res => res.json())
        .then((data) => {
            displayProduct(data);
        });
};

const displayProduct = (produats) => {
    productContaine = document.getElementById("product_container");

    produats.forEach((product) => {
        console.log(product);
        const div = document.createElement("div");
        div.classList.add("card")

        div.innerHTML = `
            <img class="card_img" src=${product.image} alt="" />
            <h5>${product.title}</h5>
            <h3>${product.price}</h3>
            <p>${product.description}</p>
            <button onclick="singleProduct('${product.id}')">Details</button>
            <button onclick="handleAddToCart('${product.title.slice(0, 12)}'    , ${product?.price})">Add To Cart</button>
            `;
        productContaine.appendChild(div);
    });
};

let count = 0;
const handleAddToCart = (name, price) => {
    const cartCount = document.getElementById("count").innerText;
    let convertedCount = parseInt(cartCount);

    convertedCount += 1;
    document.getElementById("count").innerText = convertedCount;
    console.log(convertedCount);

    const container = document.getElementById("cart_main_container");
    console.log(name, price);

    const div = document.createElement("div");
    div.classList.add("cart_info");

    div.innerHTML = `
     <p>${name}</p>
     <h3 class="price">${price}</h3>
    `;
    container.appendChild(div);
    updateTotal();
};

const updateTotal = () => {
    const allProice = document.getElementsByClassName("price");
    let count = 0;
    for (const element of allProice) {
        count = count + parseFloat(element.innerText);
    }
    document.getElementById("total").innerText = count.toFixed(2);
}

const singleProduct = (id) => {
    // console.log(id);
    fetch(`https://fakestoreapi.com/products/${id}`)
        .then(res => res.json())
        .then(json => console.log(json))
}

loadAllProduct();   