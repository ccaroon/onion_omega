var Blynk = require('/usr/bin/blynk-library');

var omega = new Blynk.Blynk('6cf5e1bd4e5d45b18c4c5a47e8aa1fbc');
var v1 = new omega.VirtualPin(1);
var v2 = new omega.VirtualPin(2);

v1.on('write', function(params) {
	console.log(params);
	v2.write(new Date().getSeconds());
});


v2.on('read', function() {
	v2.write(new Date().getSeconds());
});
