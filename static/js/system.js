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
        if (document.querySelector("#ifm0") != null) {
            document.querySelector("#ifm0").remove()
        }else {
            const ifm = document.createElement("iframe");
            ifm.setAttribute("id", "ifm0");
            ifm.src = "userlookup/0";
            addc.appendChild(ifm);
        }
        
    });
    
});
