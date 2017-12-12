
// data collection part

// This activates the mindwave, writes the collected data to a 
// CSV file and the console for a given amount of time and then 
// closes the application again once time is up.

var Mindwave = require('mindwave');
var mw = new Mindwave();
const fs = require('fs');
const file = fs.createWriteStream('rawdataHouse7.csv');
var settimer = 615000; // set timer here (miliseconds) 
// good idea to set 15 seconds buffer time
// 615000 ms = 615 seconds -> 10 min data + 15 buffer in the beginning


mw.on('wave', function(wave){
	var waveData = String(wave);
	var concatString = waveData + "\n";
	file.write(concatString);
})

console.log('Mindreading Machine v0.1');
console.log('connecting');
mw.connect('/dev/cu.MindWaveMobile-DevA');


setTimeout(function(){
	mw.removeAllListeners('wave');
	process.exit();
}, settimer);



