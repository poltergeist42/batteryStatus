from distutils.core import setup
import py2exe, os, wmi, argparse

setup( console=[{"script": "batteryStatus.py"}] )