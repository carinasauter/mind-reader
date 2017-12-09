
// data analysis

// this reads a lifestream of data, runs it 
// against the model and outputs result


//  my Mindwave device using the npm library
var Mindwave = require('mindwave');
var mw = new Mindwave();
const fs = require('fs');


console.log('Mindreading Machine v0.1');
mw.connect('/dev/cu.MindWaveMobile-DevA');
console.log('Mind Reading in progress');

buf = [];

mw.on('wave', function(wave){
	var waveData = String(wave);
	buf.push(waveData);
	// child_process.exec(command[, options][, callback])
	if (buf.length >= 512) {
		const exec = require('child_process').exec;
		console.log("calling model.")
		var input = JSON.stringify(buf);
		// console.log("input is: " + input)
		// '"/path/to/test file/test.sh" arg1 arg2'
		var cmd = 'python mindreadingmachine.py ' + input;
		exec(cmd, (err, stdout, stderr) => {
			if (err) {
				console.error(`exec error: ${err}`);
				return;
			}
			console.log('Model says: ' + stdout);
		});
		buf = [];
	}
});


// setTimeout(function(){
// 	mw.removeAllListeners('wave');
// 	file.end('done writing');
// 	process.exit();
// }, 20000);



