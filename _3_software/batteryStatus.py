#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
   :Nom du fichier:     batteryStatus.py
   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            20161206

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

# Getting Battery Capacity Windows with Python

# source : http://stackoverflow.com/questions/16380394/getting-battery-capacity-windows-with-python

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
        print( "Charged Capacity: {} mWh".format(v_batFull))

    batts = t.ExecQuery('Select * from BatteryStatus where Voltage > 0')

    for i, b in enumerate(batts):
        # print( '\nBattery %d ***************' % i )
        # print( 'Tag:               ' + str(b.Tag) )
        print( "Name:               \t{}".format(b.InstanceName ))

        print( "PowerOnline:        \t{}".format(b.PowerOnline) )
        # print( 'Discharging:       \t', b.Discharging)
        print( "Charging:           \t{}".format(b.Charging))
        # print( 'Voltage:           \t', b.Voltage)
        print( "DischargeRate:      \t{}".format(b.DischargeRate))
        print( "ChargeRate:         \t{}".format(b.ChargeRate))
        print( "RemainingCapacity:  \t{}".format(b.RemainingCapacity))
        # print( 'Active:            \t', b.Active)
        # print( 'Critical:          \t', b.Critical)
        print( "ChargeLvel (%)      \t{}%".format(round(((b.RemainingCapacity*100) /v_batFull), 2 )))

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
 