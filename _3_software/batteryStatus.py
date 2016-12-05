#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
   :Nom du fichier:     batteryStatus.py
   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            20161205

----

   :Licence:            CC-BY-NC-SA
   :Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/

----

    :dev language:      Python 3.4
    
----

lexique
-------

   :v_:                 variable
   :l_:                 list
   :t_:                 tuple
   :d_:                 dictionnaire
   :f_:                 fonction
   :C_:                 Class
   :i_:                 Instance
   :m_:                 Module
"""
#################### Taille maximum des commentaires (90 caracteres)######################

# Get power status of the system using ctypes to call GetSystemPowerStatus

# source : http://stackoverflow.com/questions/6153860/in-python-how-can-i-detect-whether-the-computer-is-on-battery-power

from os import system
import wmi

c = wmi.WMI()
t = wmi.WMI(moniker = "//./root/wmi")

batts1 = c.CIM_Battery(Caption = 'Portable Battery')

for i, b in enumerate(batts1):
    print( 'Battery %d Design Capacity: %d mWh' % (i, b.DesignCapacity or 0) )




def f_batInfo () :

    v_batFull = False
    batts = t.ExecQuery('Select * from BatteryFullChargedCapacity')
    for i, b in enumerate(batts):
        v_batFull = b.FullChargedCapacity
        print( ('Battery %d Fully Charged Capacity: %d mWh' % 
              (i, b.FullChargedCapacity)) )

    batts = t.ExecQuery('Select * from BatteryStatus where Voltage > 0')

    for i, b in enumerate(batts):
        print( '\nBattery %d ***************' % i )
        print( 'Tag:               ' + str(b.Tag) )
        print( 'Name:              ' + b.InstanceName )

        print( 'PowerOnline:       \t' + str(b.PowerOnline) )
        print( 'Discharging:       \t' + str(b.Discharging) )
        print( 'Charging:          \t' + str(b.Charging) )
        print( 'Voltage:           \t' + str(b.Voltage) )
        print( 'DischargeRate:     \t' + str(b.DischargeRate) )
        print( 'ChargeRate:        \t' + str(b.ChargeRate) )
        print( 'RemainingCapacity: \t', b.RemainingCapacity)
        print( 'Active:            \t' + str(b.Active) )
        print( 'Critical:          \t' + str(b.Critical) )
        print( (b.RemainingCapacity*100) /v_batFull )

# def f_printBF() :
    # """
    # banniere realise depuis le site :
    # http://www.network-science.de/ascii/
    # """
    # system("cls")
    # print("\n\n")
    # print("\t######                                         ")
    # print("\t#     #   ##   ##### ##### ###### #####  #   # ")
    # print("\t#     #  #  #    #     #   #      #    #  # #  ")
    # print("\t######  #    #   #     #   #####  #    #   #   ")
    # print("\t#     # ######   #     #   #      #####    #   ")
    # print("\t#     # #    #   #     #   #      #   #    #   ")
    # print("\t######  #    #   #     #   ###### #    #   #   ")
    # print("\t                                               ")
    # print("\t         #######                               ")
    # print("\t         #       #    # #      #               ")
    # print("\t         #       #    # #      #               ")
    # print("\t         #####   #    # #      #               ")
    # print("\t         #       #    # #      #               ")
    # print("\t         #       #    # #      #               ")
    # print("\t         #        ####  ###### ######          ")
    # print("\n\n")



def main() :
    f_batInfo()


if __name__ == '__main__':
    main()
 