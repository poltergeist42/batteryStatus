from distutils.core import setup
import py2exe, os, wmi, argparse, win32com

#    * Ouvrir un terminal et executer la commande suivante
#        ::
#    
#            steup.py py2exe
#        
#        Si tout c'est bien passé, un dossier nomé : "dist", contenant l'éxécutable et les
#        et les DLL, doit avoir été créer.

setup( console=[{"script": "batteryStatus.py"}] )