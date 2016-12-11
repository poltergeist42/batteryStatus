#!/usr/bin/env python3
import sys
from time import sleep
 
battery_status_file = "/proc/acpi/battery/BAT0/state"
print("Monitoring battery status. Press <Ctrl>+C to exit.")
 
try:
   with open(battery_status_file) as state:
      while True:
         state.seek(0)
         for line in state:
             data = line.split(":")[1].strip().split(" ")[0]
             if "present rate" in line:
                 if "unknown" in data:
                     rate = 0
                 else:
                     rate = int(data)
             elif "remaining" in line:
                 remaining = int(data)
                 break
 
         if not rate:
            print("\rNo statistics available.                         ", end="")
         else:
            time_left = float(remaining) / rate
            hours = int(time_left)
            minutes = int((time_left - hours) * 60)
            print("\rRemaining time left: {0} hours {1} minutes.".format(hours, minutes), end="")
         sys.stdout.flush()
         sleep(1)
except KeyboardInterrupt:
   print("\nCtrl+C pressed. Exiting.")
#- See more at: http://www.chandrashekar.info/code-vault/program-to-monitor-battery-status-using-python.html#sthash.zuEi29sl.dpuf