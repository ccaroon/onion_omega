var Blynk = require('/usr/bin/blynk-library');

var omega = new Blynk.Blynk('6cf5e1bd4e5d45b18c4c5a47e8aa1fbc');
var v1 = new omega.VirtualPin(1);
var v2 = new omega.VirtualPin(2);

var startedAt = 1484415000 * 1000;
v1.on('write', function(params) {
    console.log(params);
});


v2.on('read', function() {
    var d = durationToString(startedAt, Date.now());
    console.log(d);
    v2.write(d);
});


function durationToString(start, end) {

    // duration between start & end in seconds
    var duration = (end - start) / 1000.0;

    var days = Math.floor(duration / 86400);
    days < 10 ? days = "0"+days : '';
    duration = duration % 86400;

    var hours = Math.floor(duration / 3600);
    hours < 10 ? hours = "0"+hours : '';
    duration = duration % 3600;

    var mins = Math.floor(duration / 60);
    mins < 10 ? mins = "0"+mins : '';
    var secs = Math.floor(duration % 60);
    secs < 10 ? secs = "0"+secs : '';

    var dStr = days + ":" + hours + ":" + mins + ":" + secs;

    return (dStr);
}

