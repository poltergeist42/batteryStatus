#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Infos
=====

   :Nom du fichier:     fakeLib.py
   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            20161212

####

   :Licence:            CC-BY-NC-SA
   :Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/

####

    :dev language:      Python 3.4
    
####

lexique
=======

   :**v_**:                 variable
   :**l_**:                 list
   :**t_**:                 tuple
   :**d_**:                 dictionnaire
   :**f_**:                 fonction
   :**C_**:                 Class
   :**i_**:                 Instance
   :**m_**:                 Matrice
   
   
####

Liste des libs
==============

    - os
    - wmi
    - argparse
    
####
   
objectif
========

    BatteryStatus permet de controller le niveau de charge de la battery 
    des ordinateur portables (sous environement Microsoft).
    Lorsque le PC est complètement charger, un message apparait à l'écran pour nous
    le signaler. On peut alors débrancher l'alimentation pour travailler sur la battery.
    Cela permet de preserver la duree de vie de la battery.
    
####
    
"""

# Getting Battery Capacity Windows with Python

# source : http://stackoverflow.com/questions/16380394/getting-battery-capacity-windows-with-python

from os import system
import wmi
import argparse

c = wmi.WMI()
t = wmi.WMI(moniker = "//./root/wmi")

batts1 = c.CIM_Battery(Caption = 'Portable Battery')

for i, b in enumerate(batts1):
    print( 'Battery %d Design Capacity: %d mWh' % (i, b.DesignCapacity or 0) )



class C_BatteryStatus( object ) :
    """
    """
    def __init__( self, v_levelChk = 100 ) :
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
        self.f_setBatteryValue()
        
    def __del__( self ) :
        """ **__del__()**
        
            Permet de terminer proprement l'instance de la Class courante
        
            il faut utilise : ::
            
                del [nom_de_l'_instance]
                
            *N.B :* Si l'instance n'est plus utilisee, cette methode est appellee 
            automatiquement.
        """
        
        ## Action
        v_className = self.__class__.__name__
       

    def f_setBatteryValue( self ) :
        """ Permet d'initialiser les variables de la batterie """
        # print( "petit poucet" )
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
        

    def f_printBF(self) :
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

    def f_levelChk( self ) :
        """ Test si le taux de charge et supprérieur ou égal à la valeur de v_levelChk
            
            Si la battery n'est plus en charge (not self.Charging) et que le PC est
            toujours relier à l'alimentation, le message s'affichera tous de même
        """
        if (    (self.PowerOnline and (self.ChargeLvel >= self.v_levelChk)) 
                or ( self.PowerOnline and not self.Charging )) :
            system("cls")
            self.f_printBF()
            self.f_printBatteryValue()
            input("\n\t Appuyer sur une touche pour fermer la fenêtre")

        else :
            print( "{} - {}".format(self.ChargeLvel, self.v_levelChk))
            

def main() :
    """ Fonction principale """
    
    v_helpSetLevel = """
    Reglage du niveau de charge de la batterie.
    Cette valeur permet de changer le niveau a surveiller.
    Lorsqu'elle est atteinte, l'alerte se met en route.
    Si cette option n'est pas selectionne, le niveau par defaut est 100 %
    """
    
    # v_helpDbg = """ Cette option n'est pas implementee pour le moment """
      
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument( "-d", "--debug", action='store_true', help="Cette option n'est pas implementee pour le moment")
    parser.add_argument( "-S", "--setlevel", type=int, help=v_helpSetLevel)
                        
    args = parser.parse_args()
    
    if args.setlevel :
        batt = C_BatteryStatus(v_levelChk = args.setlevel)
        
    else :
        batt = C_BatteryStatus()
        
    batt.f_levelChk()
    

if __name__ == '__main__':
    main()
 