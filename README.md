# VideoToFrames

!pip install --upgrade opencv-python
!pip install opencv-python moviepy

!pip install scipy

!python3 extract_frames.py Arithmtique.mp4 #name_of_the_video

#After the execution of the above command, a new folder "NameOfTheVideo-opencv" is created where you can find all the frames
#Pour télécharger vidéo dll: afficher le code source du cadre, ouvrir le lien vimeo et utiliser l'extension professional video downloader

!python3 remove_doubles.py

now we have the function that splits video to frame an the one that deletes double frames
we now have to pass the directory as argument and import the second function
