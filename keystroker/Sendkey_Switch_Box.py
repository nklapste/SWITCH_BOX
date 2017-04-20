import SendKeys
import serial
import string
import time


def start_setup():
    print("\nSTARTING ARDUINO SERIAL KEYSENDER V 1.0\n")
    print("Input additional port options as needed.\
    \nLeave blank if you want to run default.")

    print("PORT:", end=" ")
    port = input()

    if port == "":
        port = 'COM5'

    print("BAUDRATE:", end=" ")
    baudrate = input()

    if baudrate == "":
        baudrate = 9600
    else:
        baudrate = int(baudrate)
    print("\nSelected port settings:")
    print("PORT:", port)
    print("BAUDRATE:", baudrate)

    ser = serial.Serial(port, baudrate)
    ser.open()

    return ser


def sendkey_char(char_in=None):
    if char_in is None:
        print("ERROR: NO INPUT")
        return

    print("Recieved Input:", char_in)
    print("Printing...")

    SendKeys.SendKeys(char_in)
    time.sleep(0.2)


def serial_read_switch(ser, mapped_keys=None):
    if mapped_keys is None:
        # sets mapped_keys to all lowercase strings
        mapped_keys = set(string.ascii_lowercase)

    while True:
        for line in ser.readline():
            de_char = line.decode(encoding='UTF-8', errors='strict')

            if de_char == "EXIT":
                print("QUITING SIGNAL SENT: EXITING")
                return

            elif de_char in mapped_keys:
                sendkey_char(de_char)
            else:
                print("ERROR: INCORRECT KEY SENT")


if __name__ == '__main__':
    ser = start_setup()
    serial_read_switch(ser)
