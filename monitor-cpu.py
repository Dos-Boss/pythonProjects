import os
import time

def measure_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    return (temp.replace("temp=", ""))

def get_clock_speed():
    read_speed = os.popen("vcgencmd measure_clock arm").readline().replace("frequency(48)=", "")
    clock_speed = str(round(int(read_speed)/1000000, 0)).replace (".0", "")
    return (clock_speed)

while True:
    print(get_clock_speed()+"Mhz")
    print(measure_temp())

    time.sleep(1)
