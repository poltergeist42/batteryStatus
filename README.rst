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
    
Instructions
============

    Pour utiliser cette apply il faut en créer une version standalone à l'aide de py2exe.
    
        #. Installer py2exe
            ::
    
                pip install py2exe
        
        #. Générer le fichier binaire
        
            * Se placer dans :
                ::
            
                    ./_3_software/
                
            * Ouvrir un terminal et executer la commande suivante
                ::
            
                    steup.py py2exe
                
                Si tout c'est bien passé, un dossier nomé : "dist"
                doit avoir été créer.
                
        #. Mettre en place la tache planifié
        
            * Créer une nouvelle tache planifier
            * selectionner ouvrir une application puis choisissez l'application "batteryStatus.exe"
              qui se trouve dans le dossier "dist"
            * choisissez une periode (tous les jours) puis dans les propriétés avancées,
              choisissez une fréquences d'execution toutes les 5 ou 15 minutes
            * Valider et attendez. Lorsque votre battery sera complétement chargée,
              un message apparaitra sur votre ecran.
