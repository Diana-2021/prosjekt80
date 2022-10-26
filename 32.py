#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 09:45:23 2022

@author: rezanmoustafa
"""

lengde_meter=1/0.3048
antall_meter=input("brukeren skal skriv inn antall meter :")
antall_meter1=float(antall_meter)
antall_fot=antall_meter1*lengde_meter
print("antall fot:", end="")
print(antall_fot)