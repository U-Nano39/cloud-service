console.log("Welcome to Qvey's Website.")

const ul0 = document.querySelector("#list0")

ul0.addEventListener("mouseover", function() {
    ul0.style.textDecoration = "underline";
});

ul0.addEventListener("mouseleave", function() {
    ul0.style.textDecoration = "none";
})
