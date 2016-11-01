# -*- coding: utf-8 -*-         # Permet d'écrire les accents et les caractères spéciaux

import os
import exiftool
import time

StartClock = time.time()        # Permet de voir le temps mis par le script
CountDone = 0                   # Permet de compter le nombre de fichiers traités
ImgPath2Title_Log = open("IPTC-_Log.txt", "w")  # Fichier log enregistrant les fichiers traités

with exiftool.ExifTool() as et:
	for dirpath, subdirs, files in os.walk(os.getcwd()):    # Boucle sur tous les sous-dossiers
		for line in files:                              # Boucle sur tous les fichiers
			if line.endswith((".jpg", ".JPG", ".jpeg", ".JPEG", ".tif", ".TIF", ".tiff", ".TIFF")): # Seuls ces formats d'image sont pris en considération.
				ImagePath = os.path.join(dirpath, line)         # Enregistrement du chemin d'accès dans une variable
				et.execute(                                     # Modifier les données IPTC ici (tout ce qui est en vert avec IDLE
					"-iptc:ReleaseDate=20130604",
					"-iptc:ReleaseTime=100006",
					"-iptc:ExpirationDate=20130604",
					"-iptc:ExpirationTime=100006",
					"-iptc:City=Avenches",
					"-iptc:Province-State=VD",
					"-iptc:Country-PrimaryLocationCode=CH",
					"-iptc:Country-PrimaryLocationName=Suisse",
					"-iptc:headline="+ImagePath,            # Le chemin d'accès au fichier dans le Titre
					"-iptc:keywords=Tag1",
					"-iptc:keywords=Tag2",
					"-iptc:keywords=Tag3",
					"-iptc:keywords=Tag4",
					"-iptc:keywords=Tag5",
					"-iptc:SupplementalCategories=Labo",
					"-iptc:Credit=Site et Musée Romains d'Avenches",
					"-iptc:Source=Prise de vue numérique",
					"-iptc:CopyrightNotice=Copyright © - 2016 - Site et Musée Romains d'Avenches",
					"-iptc:Contact=musee.romain@vd.ch",
					ImagePath)                              # Indique quelle image est à modifier. Ne pas toucher!
				ImgPath2Title_Log.write(ImagePath + "\n")       # Inscription du fichier traité dans le Log
				CountDone = CountDone + 1			# Une image de plus!
				print ImagePath, "DONE"				# Affiche le fichier traité dans la console


StopClock = time.time()
TotalTime = round(StopClock - StartClock,1)                                     # Temps mis par le script
TimeLog = str(CountDone) + ' images treated in ' + str(TotalTime) + ' seconds'  # Variable: phrase indiquant le temps

print TimeLog                                                                   # Inscrire le temps sur la console

ImgPath2Title_Log.write(TimeLog)                                                # Inscrire le temps dans le log
ImgPath2Title_Log.close()
