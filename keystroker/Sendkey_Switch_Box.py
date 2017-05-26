import SendKeys
import serial
import string
import argparse

def start_setup():


    parser = argparse.ArgumentParser(description="SWITCH BOX KEYSENDER SETUP")

    group = parser.add_argument_group(title="Serial communication config")
    group.add_argument("-p", "--port", help="set the serial port of the arduino",
                       default='COM3')
    group.add_argument("-b", "--baudrate", help="set the communication baudrate",
                       default=9600)
    group.add_argument("-t", "--timeout", help="set the timeout value for the serial communication",
                       default=0.5)

    args = parser.parse_args()

    port = args.port
    baudrate = args.baudrate
    timeout = args.timeout

    print("Selected port settings:")
    print("PORT:", port)
    print("BAUDRATE:", baudrate)
    print("TIMEOUT:", timeout)


    ser = serial.Serial(port, baudrate)
    ser.timeout = timeout
    return ser


def sendkey_char(char_in=None):
    if char_in is None:
        print("ERROR: NO INPUT")
        return

    print("RECIEVED:", char_in)
    SendKeys.SendKeys(char_in)


def serial_read_switch(ser, mapped_keys=None):
    if mapped_keys is None:
        # sets mapped_keys to all lowercase strings
        mapped_keys = set(string.ascii_lowercase)

    mssg = []
    de_char = None

    while True:
        # for line in ser.readlines():
            # mssg = line.strip()

        for line_p in ser.readline():  # TODO SWITCH TO READLINES

            if chr(line_p) == "\n":
                de_char = "".join(mssg)
                de_char = de_char.strip()
                mssg = []
            else:
                mssg.append(chr(line_p))

            if de_char is not None:
                if de_char == "EXIT":
                    print("QUITING SIGNAL SENT: EXITING")
                    return

                elif de_char in mapped_keys:
                    sendkey_char(de_char)
                else:
                    print("ERROR: INCORRECT KEY SENT:", de_char)

                de_char = None


if __name__ == '__main__':
    ser = start_setup()
    serial_read_switch(ser)
