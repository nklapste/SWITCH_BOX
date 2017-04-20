import SendKeys
import time


print("starting keysroker...")


while True:
    line = input()

    if line == "EXIT":
        break

    if line == "LOOP":
        line = input()
        for i in range(20):
            SendKeys.SendKeys(line)
    else:

        SendKeys.SendKeys(line)
