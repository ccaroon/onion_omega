#!/usr/bin/env node
//---------------------------------------------------------------------------------
var Blynk = require('/usr/bin/blynk-library');
var LED = require("omega_gpio").LED;

var led = new LED(1);

var omega = new Blynk.Blynk('6cf5e1bd4e5d45b18c4c5a47e8aa1fbc');
var v1 = new omega.VirtualPin(1);
var v2 = new omega.VirtualPin(2);
var v3 = new omega.VirtualPin(3);

//var startedAt = Date.parse("Jan 14, 2017 12:30");
var startedAt = Date.parse("Feb 19, 1971 4:30");

v1.on('write', function(params) {
    console.log("V1 Pushed");
    startedAt = Date.now();
});


v2.on('read', function() {
    var d = durationToString(startedAt, Date.now());
    v2.write(d);
});

v3.on('write', function(params) {
    console.log("V3:" + params);
    led.toggle();
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

process.on('SIGINT', function(){
    led.destroy();
    process.exit();
});
