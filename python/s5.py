# To create a countdown timer
import time


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        TimeFormat = '{:02d}:{:02d}'.format(mins, secs)
        print(TimeFormat, end='\r')
        time.sleep(1)
        time_sec -= 1

        print("Counting: ", time_sec)


num = int(input("Set your timer in Sec: "))

countdown(num)
