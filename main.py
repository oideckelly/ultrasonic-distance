serial.redirect_to_usb()
serial.set_baud_rate(BaudRate.BAUD_RATE115200)

distance = 0
radio.set_group(99)

def on_forever():
    global distance
    distance = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.CENTIMETERS)

#use show distance for test purposes

    basic.show_number(distance)
    #Sends Distance value to receiver microbit
    radio.send_number(distance)
    #writes value of Distance into CSV file
    serial.write_numbers([distance])
    timeanddate.seconds_since_reset()
    #writes value of Time since microbitstart + "Time" so that i can clearly identify it in the CSV file
    serial.write_line("time"+(timeanddate.seconds_since_reset()))

    basic.pause(100)
basic.forever(on_forever)

