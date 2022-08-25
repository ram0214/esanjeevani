
var recognition = new webkitSpeechRecognition();

recognition.onresult = function(event) { 
    console.log('result');
    var saidText = "";
    for (var i = event.resultIndex; i < event.results.length; i++) {
        if (event.results[i].isFinal) {
            saidText = event.results[i][0].transcript;
        } else {
            saidText += event.results[i][0].transcript;
        }
    }

    document.getElementById('speechText').value = saidText;
    searchPosts(saidText);
}

function startRecording(){
  recognition.start();
}

function searchPosts(saidText){

  $.ajax({
    url: 'getData.php',
    type: 'post',
    data: {speechText: saidText},
    success: function(response){
      $('.container').empty();
      $('.container').append(response);
    }
  });
}