serial.redirectToUSB()
serial.setBaudRate(BaudRate.BaudRate115200)
let distance = 0
radio.setGroup(99)
basic.forever(function on_forever() {
    
    distance = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.Centimeters)
    // use show distance for test purposes
    basic.showNumber(distance)
    // Sends Distance value to receiver microbit
    radio.sendNumber(distance)
    // writes value of Distance into CSV file
    serial.writeNumbers([distance])
    timeanddate.secondsSinceReset()
    // writes value of Time since microbitstart + "Time" so that i can clearly identify it in the CSV file
    serial.writeLine("time" + timeanddate.secondsSinceReset())
    basic.pause(100)
})
