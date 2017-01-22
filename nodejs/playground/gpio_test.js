#!/usr/bin/env node
//---------------------------------------------------------------------------------
var LED = require("omega_gpio").LED;

var led = new LED(1);

led.toggle();

process.on('SIGINT', function(){
    led.destroy();
    process.exit();
});
