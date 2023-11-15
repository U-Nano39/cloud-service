console.log("Welcome to Qvey's Website.")


window.addEventListener("DOMContentLoaded", function() {
  
    const InputArea = document.querySelector("#InputArea");
    const search = document.querySelector("#search");

    InputArea.onkeypress = function(event){
        if (event.key === 'Enter') {
            const ID = InputArea.value;
            location.href = ID;
            };
        };

    search.addEventListener("click", function() {
        const ID = InputArea.value;
        location.href = ID;
    });
});
