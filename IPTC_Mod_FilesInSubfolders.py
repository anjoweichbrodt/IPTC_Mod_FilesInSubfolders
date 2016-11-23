# -*- coding: utf-8 -*-         # Permet d'écrire les accents et les caractères spéciaux

import os
import exiftool
import time
import re
import Tkinter, tkFileDialog

root = Tkinter.Tk()
root.withdraw()
dirname=os.path.normpath(tkFileDialog.askdirectory(parent=root,title="Selectionner le dossier")).encode('ascii') # Sans l'encoding ascii ca se passe mal, ca doit venir de l'interfacage avec la lib exiftool
configFileName=os.path.join(dirname, "exif.txt")
validConfigLine=re.compile("^([^#].+?)(#|$)") # Afin de supporter les commentaires dans le fichier de config (#)

if not dirname:
        raise "Il faut choisir un dossier"

if not os.path.exists(configFileName):
        configFileName=tkFileDialog.askopenfilename(parent=root,title="Selectionner le fichier exif",filetypes=(("All files", "*.*"),("Text files", "*.txt")))

if not configFileName:
        raise "Il faut choisir un fichier exif"

# Lecture des parametre depuis le fichier de config
settings=["-overwrite_original"]
with open(configFileName) as f:
        for line in f:
                m=validConfigLine.match(line)
                if m:
                        settings.append(m.groups()[0])
StartClock = time.time()        # Permet de voir le temps mis par le script
CountDone = 0                   # Permet de compter le nombre de fichiers traités
ImgPath2Title_Log = open("IPTC-_Log.txt", "w")  # Fichier log enregistrant les fichiers traités

with exiftool.ExifTool() as et:
	for dirpath, subdirs, files in os.walk(dirname):    # Boucle sur tous les sous-dossiers
		for line in files:                              # Boucle sur tous les fichiers
			if line.lower().endswith((".jpg", ".jpeg", ".tif", ".tiff")): # Seuls ces formats d'image sont pris en considération.
				ImagePath = os.path.join(dirpath, line)
				fileSettings= map(lambda x: x.replace("%ImagePath%",ImagePath),settings)
				et.execute(*(fileSettings+[ImagePath]))
				ImgPath2Title_Log.write(ImagePath + "\n")       # Inscription du fichier traité dans le Log
				CountDone+=1
				print ImagePath, "DONE"				# Affiche le fichier traité dans la console


StopClock = time.time()
TotalTime = round(StopClock - StartClock,1)                                     # Temps mis par le script
TimeLog = str(CountDone) + ' images treated in ' + str(TotalTime) + ' seconds'  # Variable: phrase indiquant le temps

print TimeLog                                                                   # Inscrire le temps sur la console

ImgPath2Title_Log.write(TimeLog)                                                # Inscrire le temps dans le log
ImgPath2Title_Log.close()

