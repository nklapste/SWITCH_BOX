import SendKeys
import serial
import string
import time


def start_setup():
    print("\nSTARTING ARDUINO SERIAL KEYSENDER V 1.0\n")
    print("Input additional port options as needed.\
    \nLeave blank if you want to run default.\n")

    print("PORT:", end=" ")
    port = input()
    if port == "":
        port = 'COM3'

    print("BAUDRATE:", end=" ")
    baudrate = input()
    if baudrate == "":
        baudrate = 9600
    else:
        baudrate = int(baudrate)

    print("TIMEOUT:", end=" ")
    timeout_val = input()
    if timeout_val == "":
        timeout_val = 0.5
    else:
        timeout_val = float(timeout_val)

    print("\nSelected port settings:")
    print("PORT:", port)
    print("BAUDRATE:", baudrate)
    print("TIMEOUT:", timeout_val)
    print("")

    ser = serial.Serial(port, baudrate)
    ser.timeout = timeout_val
    return ser


def sendkey_char(char_in=None):
    if char_in is None:
        print("ERROR: NO INPUT")
        return
    print("RECIEVED:", char_in)
    SendKeys.SendKeys(char_in)
    time.sleep(0.2)


def serial_read_switch(ser, mapped_keys=None):
    if mapped_keys is None:
        # sets mapped_keys to all lowercase strings
        mapped_keys = set(string.ascii_lowercase)

    mssg = []
    de_char = None

    while True:
        for line_p in ser.readline():

            if chr(line_p) == "\n":
                de_char = "".join(mssg)
                mssg = []
            else:
                mssg.append(chr(line_p))

            if not de_char is None:
                if de_char == "EXIT":
                    print("QUITING SIGNAL SENT: EXITING")
                    return

                elif de_char in mapped_keys:
                    sendkey_char(de_char)
                else:
                    print("ERROR: INCORRECT KEY SENT")

                de_char = None


if __name__ == '__main__':
    ser = start_setup()
    serial_read_switch(ser)
