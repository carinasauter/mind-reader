
// data collection part

// This activates the mindwave, writes the collected data to a 
// CSV file and the console for a given amount of time and then 
// closes the application again once time is up.

var Mindwave = require('mindwave');
var mw = new Mindwave();
const fs = require('fs');
const file = fs.createWriteStream('rawdata.csv');
var settimer = 615000; // set timer here (miliseconds) 
// good idea to set 15 seconds buffer time
// 615000 ms = 615 seconds -> 10 min data + 15 buffer in the beginning


mw.on('wave', function(wave){
	var waveData = String(wave);
	// var timeData = String(Date.now());
	// var concatString = waveData + ',' + timeData + "\n"; // necessary because asynchronous
	file.write(waveData + "\n", encoding='utf8');
	console.log(waveData);
})

console.log('Mindreading Machine v0.1');
console.log('connecting');
mw.connect('/dev/cu.MindWaveMobile-DevA');
var start = Date.now();


setTimeout(function(){
	mw.removeAllListeners('wave');
	process.exit();
}, settimer);



