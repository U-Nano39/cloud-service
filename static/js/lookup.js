console.log("Welcome to Qvey's Website.")


window.addEventListener("DOMContentLoaded", function() {
  
    const InputArea = document.querySelector("#InputArea");
    const search = document.querySelector("#search");

    search.addEventListener("click", function() {
        const ID = InputArea.value;
        location.href = "userlookup/"+ID;
    });
});
