import cv2
import os

video_dizin="C:/Users/YUNUS/Desktop/ornek.mp4" #Videonun bulunduğu dizin

masaustu=os.path.join(os.path.expanduser("~"),"Desktop")
dizin=os.path.join(masaustu,"Resimler")

if os.path.exists(dizin):
    resim_dosya=os.path.join(os.path.expanduser("~"),"Desktop","Resimler")
else:
    os.makedirs(dizin)
    resim_dosya=os.path.join(os.path.expanduser("~"),"Desktop","Resimler")

cap=cv2.VideoCapture(video_dizin)

fps=cap.get(cv2.CAP_PROP_FPS)
toplam=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

for i in range(0,toplam,int(fps)):
    cap.set(cv2.CAP_PROP_POS_FRAMES,i)
    j,k=cap.read()

    if j:
        resim=os.path.join(resim_dosya, f"resim_{i}.jpg")
        cv2.imwrite(resim,k)

cap.release()

