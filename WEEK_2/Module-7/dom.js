
// // const target = document.getElementsByClassName("title");
// const target = document.getElementById("title");
// console.log(target);

// target.style.color = "red";

// const allBox = document.getElementsByClassName("box");
// for (let i = 0; i < allBox.length; i++) {
//     const element = allBox[i];
//     element.style.backgroundColor = "green";

//     if (element.innerText == "box-5") {
//         element.style.backgroundColor = "red";
//     }
// }

document.getElementById("handleAdd").addEventListener("click", (event) => {
    const inputValue = document.getElementById("search_box").value;

    const container = document.getElementById("comment_container");

    const p = document.createElement("p");
    p.classList.add("child");
    p.innerText = inputValue;

    container.appendChild(p);
    document.getElementById("search_box").value = "";

    const allComments = document.getElementsByClassName("child");


    for (const element of allComments) {
        element.addEventListener("click", (e) => {
            console.log(e.target.parentNode.removeChild(element));
        });
    }
});

fetch("https://jsonplaceholder.typicode.com/users")
    .then(res => res.json())
    .then(data => {
        displayData(data);
    })
    .catch(err => {
        console.log(err);
    });

const displayData = (userData) => {
    const container = document.getElementById("userData_container");

    userData.forEach(user => {
        const div = document.createElement("div");

        div.classList.add("user")

        div.innerHTML = `
            <h1>Title</h1>
            <p>Description</p>
            <button>Details</button>
        `;
        container.appendChild(div);
    });
};