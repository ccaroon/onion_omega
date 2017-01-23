#!/usr/bin/env node
/******************************************************************************/
const Blynk = require('/usr/bin/blynk-library');
const fs    = require('fs');

var omega = new Blynk.Blynk('6cf5e1bd4e5d45b18c4c5a47e8aa1fbc');
var resetButton = new omega.VirtualPin(1);
var brewTime    = new omega.VirtualPin(2);
var temperature = new omega.VirtualPin(3);

var startedAt = Date.parse("Jan 14, 2017 12:30");

resetButton.on('write', function(params) {
    startedAt = Date.now();
    updateBrewTime();
});

setInterval(function() {
    updateBrewTime();
    updateTemperature();
}, 5000);

function updateBrewTime() {
    var d = durationToString(startedAt, Date.now());
    brewTime.write(d);
}

function updateTemperature() {
    var data = fs.readFileSync('/sys/devices/w1_bus_master1/28-000006576fb0/w1_slave', 'utf8');
    var lines = data.split("\n");
    var matches = lines[1].match(/t=(\d+)/);
    var temp = matches[1]/1000.0
    temp = (temp * 1.8) + 32.0;
    temperature.write(Math.round(temp));
}

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
