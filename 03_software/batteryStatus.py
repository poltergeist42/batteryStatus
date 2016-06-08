# Get power status of the system using ctypes to call GetSystemPowerStatus

# source : http://stackoverflow.com/questions/6153860/in-python-how-can-i-detect-whether-the-computer-is-on-battery-power

import ctypes
from ctypes import wintypes
from os import system

class SYSTEM_POWER_STATUS(ctypes.Structure):
    _fields_ = [
        ('ACLineStatus', wintypes.BYTE),
        ('BatteryFlag', wintypes.BYTE),
        ('BatteryLifePercent', wintypes.BYTE),
        ('Reserved1', wintypes.BYTE),
        ('BatteryLifeTime', wintypes.DWORD),
        ('BatteryFullLifeTime', wintypes.DWORD),
    ]

# def f_statusInit():
SYSTEM_POWER_STATUS_P = ctypes.POINTER(SYSTEM_POWER_STATUS)
GetSystemPowerStatus = ctypes.windll.kernel32.GetSystemPowerStatus
GetSystemPowerStatus.argtypes = [SYSTEM_POWER_STATUS_P]
GetSystemPowerStatus.restype = wintypes.BOOL
status = SYSTEM_POWER_STATUS()
if not GetSystemPowerStatus(ctypes.pointer(status)):
    raise ctypes.WinError()



def f_printBF() :
    """
    banniere realise depuis le site :
    http://www.network-science.de/ascii/
    """
    system("cls")
    print("\n\n")
    print("\t######                                         ")
    print("\t#     #   ##   ##### ##### ###### #####  #   # ")
    print("\t#     #  #  #    #     #   #      #    #  # #  ")
    print("\t######  #    #   #     #   #####  #    #   #   ")
    print("\t#     # ######   #     #   #      #####    #   ")
    print("\t#     # #    #   #     #   #      #   #    #   ")
    print("\t######  #    #   #     #   ###### #    #   #   ")
    print("\t                                               ")
    print("\t         #######                               ")
    print("\t         #       #    # #      #               ")
    print("\t         #       #    # #      #               ")
    print("\t         #####   #    # #      #               ")
    print("\t         #       #    # #      #               ")
    print("\t         #       #    # #      #               ")
    print("\t         #        ####  ###### ######          ")
    print("\n\n")

    # if not GetSystemPowerStatus(ctypes.pointer(status)):
        # raise ctypes.WinError()
    print ('ACLineStatus', status.ACLineStatus)
    print ('BatteryFlag', status.BatteryFlag)
    print ('BatteryLifePercent', status.BatteryLifePercent, " - type : ", type(status.BatteryLifePercent))
    print ('BatteryLifeTime', status.BatteryLifeTime)
    print ('BatteryFullLifeTime', status.BatteryFullLifeTime)

def main() :
    print("dbgMsg : status.BatteryLifePercent : ",status.BatteryLifePercent)
    # test = status.BatteryLifePercent
    # print(test, " - ", type(test))
    if (status.ACLineStatus) and (status.BatteryLifePercent == 100) :
        f_printBF()
        # input("\nappuyer sur entree pour fermer la fenetre")
        
    input("\nappuyer sur entree pour fermer la fenetre")


if __name__ == '__main__':
    main()
 