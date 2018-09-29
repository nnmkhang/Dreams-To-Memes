console.log("Loaded");

function sendLink(){
    var text, form_id;
    form_id = document.getElementById("form");
    text = form_id.elements["text"].value;
    console.log(text);
     
    document.getElementById("demo").innerHTML = "sending" // instead of sending, display image of meme and alert user to check the printer 
}


//java script post to flask s