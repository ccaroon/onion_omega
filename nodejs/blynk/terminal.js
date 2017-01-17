var Blynk = require('/usr/bin/blynk-library');

var omega = new Blynk.Blynk('6cf5e1bd4e5d45b18c4c5a47e8aa1fbc');
var term = new omega.WidgetTerminal(4);

term.on('write', function(text) {
    console.log(text);
    term.write("You said: " + text + "\n");
});



