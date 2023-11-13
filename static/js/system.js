console.log("Welcome to Qvey's Website.")


window.addEventListener("DOMContentLoaded", function() {
    
    const ul0 = document.querySelector("#list0");

    ul0.addEventListener("mouseover", function() {
        ul0.style.textDecoration = "underline";
    });

    ul0.addEventListener("mouseleave", function() {
        ul0.style.textDecoration = "none";
    });

    ul0.addEventListener("click", function() {
        const addc = document.querySelector("#ifm");
        const ifm = document.createElement("iframe");
        ifm.setAttribute("id", "ifm0)
        ifm.src = "templates/DiscordUserLookUp.html";
        addc.appendChild(ifm);
    })
    
});
