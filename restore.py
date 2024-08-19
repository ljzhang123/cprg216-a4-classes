# Restores the txt info files to their original data
import shutil
import os

def removeReplace(backup, current):
    if os.path.exists(current):
        os.remove(current)
    shutil.copy2(backup, current)

def restoreOriginal():
    removeReplace("doctorsBackup.txt", "doctors.txt")
    removeReplace("patientsBackup.txt", "patients.txt")

restoreOriginal()