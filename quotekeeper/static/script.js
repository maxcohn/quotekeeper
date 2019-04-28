
function sendQuote(url, data){
    fetch(url, {
        method: 'POST', // or 'PUT'
        body: JSON.stringify(data), // data can be `string` or {object}!
        headers:{
          'Content-Type': 'application/json'
        }
      })
}

$(document).ready(function(){
    $("#send").click(function(){
        console.log('Sending POST');
        var data = {
            text: $("#input-text").val(),
            author: $("#input-author").val()
        };
    
        fetch('/newquote', {
            method: 'POST', // or 'PUT'
            body: JSON.stringify(data), // data can be `string` or {object}!
            headers:{
              'Content-Type': 'application/json'
            }
        });
    });
});
