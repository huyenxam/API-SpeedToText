var aud = document.getElementById("audio");
let logElement = document.getElementById("log");
var recordingTimeMS = 9000;
var input = document.getElementById("upload");
var para = document.getElementById("time");


const mapper = {};
input.addEventListener("change", handleFiles);
const ac = new AudioContext();
var count = 0;



const seconds = (number, [inMin, inMax], [outMin, outMax]) => {
    return (number - inMin) / (inMax - inMin) * (outMax - outMin) + outMin;
}


async function handleFiles(event) {
    var files = event.target.files;
    audio_path = document.getElementById("upload").files.item(0).name
    document.getElementById("path").innerHTML = audio_path
    //getTheEnergies(files);'
    var chunkSize = 50;
    const buffer = await input.files[0].arrayBuffer();
    const audioBuffer = await ac.decodeAudioData(buffer);
    const float32Array = audioBuffer.getChannelData(0);
    console.log(audioBuffer);

    let i = 0;
    const length = float32Array.length;
    while (i < length) {
        let val = float32Array.slice(i, i += chunkSize).reduce(function (total, value) {
            return Math.max(total, Math.abs(value))
        }) * 100;
        if (val > 75 || val <= 25) {

            mapper[(parseInt(seconds(i, [0, 7504986], [0, 156])))] = val;
        }
        i = i + 48000;
    }
    console.log(mapper);



    $("#src").attr("src", URL.createObjectURL(files[0]));
    aud.load();
    aud.addEventListener("loadedmetadata", () => {

        recordingTimeMS = aud.duration;
        recordingTimeMS = recordingTimeMS * 1000;
        console.log(recordingTimeMS);
    })
}



function log(msg) {
    logElement.innerHTML += msg + "\n";
}

