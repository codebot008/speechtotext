var state = -1;
URL = window.URL || window.webkitURL;

var gumStream; 						//stream from getUserMedia()
var rec; 							//Recorder.js object
var input;

// shim for AudioContext when it's not avb.
var AudioContext = window.AudioContext || window.webkitAudioContext;
var audioContext = new AudioContext(); //audio context to help us record




function startRecording(stream){
    var constraints = { audio: true, video:false };
    navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
	console.log("getUserMedia() success, stream created, initializing Recorder.js ...");
	gumStream = stream;
    input = audioContext.createMediaStreamSource(stream);
    rec = new Recorder(input,{numChannels:1});
    rec.record();
	}).catch(function(err) {
        console.log(err.message);
});
//    gumStream = stream;
//    input = audioContext.createMediaStreamSource(stream);
//    console.log("Recording started");
//    rec = new Recorder(input,{numChannels:1});
}

function stopRecording(){
    rec.stop();
    gumStream.getAudioTracks()[0].stop();
    rec.exportWAV(createDownloadLink);
}

function handlemic(){
    if(state == -1)
    {
        console.log('Now recording');
        state = state * -1;
        startRecording();
    }
    else
    {
        console.log('Stopping recording');
        state = state * -1;
        stopRecording();
    }
}

function createDownloadLink(blob) {
	var url = URL.createObjectURL(blob);
	var filename = new Date().toISOString();
	var xhr=new XMLHttpRequest();
		  xhr.onload=function(e) {
		      if(this.readyState === 4) {
		          document.getElementById("user").value = e.target.responseText;
		          console.log("Server returned: ",e.target.responseText);
		      }
		  };
    var fd=new FormData();
	fd.append("file",blob, filename);
    console.log(blob);
    xhr.open("POST","/stt",true);
    xhr.send(fd);
}


//function submit(blob) {
//  var reader = new window.FileReader();
//  reader.readAsDataURL(blob);
//  reader.onloadend = function() {
//    var fd = new FormData();
//    base64data = reader.result;
////    console.log(base64data);
//    fd.append('file', base64data, 'audio.wav');
//    console.log(file.values);
//    $.ajax({
//      type: 'POST',
//      url: '/stt',
//      data: fd,
//      cache: false,
//      processData: false,
//      contentType: false,
//      enctype: 'multipart/form-data'
//    }).done(function(data) {
//      console.log(data);
//    });
//  }
//}