#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
   :Nom du fichier:     batteryStatus.py
   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            20161207

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


class C_BatteryStatus( object ) :
    """
    """
    def __ini__( self, v_levelChk = 100 ) :
        """ initialisation des varraibles """
        self.v_levelChk                 = v_levelChk
        self.v_FullChargedCapacity      = False
        self.InstanceName               = False
        self.PowerOnline                = False
        self.Charging                   = False
        self.DischargeRate              = False
        self.ChargeRate                 = False
        self.RemainingCapacity          = False
        self.ChargeLvel                 = False
        

    def f_setBatteryValue( self ) :
        """ Permet d'initialiser les variables de la batterie """
        batts = t.ExecQuery('Select * from BatteryFullChargedCapacity')
                    # la methode : ExecQuery fait des requette SQL pour intéroger la base WMI
        for i, b in enumerate(batts):
            self.v_FullChargedCapacity = b.FullChargedCapacity

        batts = t.ExecQuery('Select * from BatteryStatus where Voltage > 0')

        for i, b in enumerate(batts):

            self.InstanceName       = b.InstanceName
            self.PowerOnline        = b.PowerOnline
            self.Charging           = b.Charging
            self.DischargeRate      = b.DischargeRate
            self.ChargeRate         = b.ChargeRate
            self.RemainingCapacity  = b.RemainingCapacity
            self.ChargeLvel         = round(((b.RemainingCapacity*100) /self.v_FullChargedCapacity), 2 )
        
    def f_printBatteryValue( self ) :
        """ Affiche les données de la batterie """
        print( "Name:               \t{}".format(self.InstanceName ))
        print( "PowerOnline:        \t{}".format(self.PowerOnline) )
        print( "Charging:           \t{}".format(self.Charging))
        print( "DischargeRate:      \t{}".format(self.DischargeRate))
        print( "ChargeRate:         \t{}".format(self.ChargeRate))
        print( "Charged Capacity:   \t{} mWh".format(self.v_FullChargedCapacity))
        print( "RemainingCapacity:  \t{}".format(self.RemainingCapacity))
        print( "ChargeLvel (%)      \t{}%".format(self.ChargeLvel))
        # print( '\nBattery %d ***************' % i )
        # print( 'Tag:               ' + str(b.Tag) )
        # print( 'Discharging:       \t', b.Discharging)
        # print( 'Voltage:           \t', b.Voltage)
        # print( 'Active:            \t', b.Active)
        # print( 'Critical:          \t', b.Critical)
        
    def f_levelChk( self ) :
        """ Test si le taux de charge et supprérieur ou égal à la valeur de v_levelChk """

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



def main() :
    f_batInfo()


if __name__ == '__main__':
    main()
 