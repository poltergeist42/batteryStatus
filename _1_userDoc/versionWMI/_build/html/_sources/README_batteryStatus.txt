=============
batteryStatus
=============

   :Autheur:          `Poltergeist42 <https://github.com/poltergeist42>`_
   :Projet:           batteryStatus
   :Licence:          CC BY-NC-SA 4.0
   :Liens:            https://creativecommons.org/licenses/by-nc-sa/4.0/ 

------------------------------------------------------------------------------------------

Description
===========

    BatteryStatus permet de controller le niveau de charge de la battery 
    des ordinateur portables (sous environement Microsoft).
    Lorsque le PC est complètement charger, un message apparait à l'écran pour nous
    le signaler. On peut alors débrancher l'alimentation pour travailler sur la battery.
    Cela permet de preserver la duree de vie de la battery.
                  
Instructions pour la version WMI
================================

Cette version nécessite que python soit installer et renseigné dans le path de la machine
               
        #. Mettre en place la tache planifié
        
            * Créer une nouvelle tache planifier
            * selectionner ouvrir une application puis choisissez le script "runIt.bat"
            * choisissez une periode (tous les jours) puis dans les propriétés avancées,
              choisissez une fréquences d'execution toutes les 5, 15 ou 20 minutes
            * Valider et attendez. Lorsque votre battery sera complétement chargée,
              un message apparaitra sur votre ecran.
