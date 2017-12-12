
// data analysis

// this reads a livestream of data from the mindwave, runs it 
// against the model (via child_process.exec function) and outputs result


var Mindwave = require('mindwave');
var mw = new Mindwave();
const fs = require('fs');


console.log('Mindreading Machine v0.1');
mw.connect('/dev/cu.MindWaveMobile-DevA');
console.log('Connecting...');

buf = [];

readings = 0;
count = 0;

found = false;

mw.on('wave', function(wave){
	var waveData = String(wave);
	buf.push(waveData);
	if (buf.length >= 512) {
		const exec = require('child_process').exec;
		var input = JSON.stringify(buf);
		var cmd = 'python mindreadingmachine.py ' + input;
		exec(cmd, (err, stdout, stderr) => {
			if (err) {
				console.error(`exec error: ${err}`);
				return;
			}
			readings = readings + 1;
			if (readings == 5) {
				console.log("Mind Reading Machine is ready.")
			}
			if (readings >=  5 & stdout != 0 & !found) {
				count = count + 1;
				console.log(count + " Model says you thought it!");
				found = true;
			} 
			if (readings >= 5 & stdout == 0 & found) {
				found = false;
			}
		});
		buf = [];
	}
});


// setTimeout(function(){
// 	mw.removeAllListeners('wave');
// 	file.end('done writing');
// 	process.exit();
// }, 20000);



