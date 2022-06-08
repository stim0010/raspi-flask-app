from gpiozero import Button
from signal import pause

btn_image = Button(12)
btn_video = Button(13)

def show_vid():
    print("Video")

def show_img():
    print("Image")

btn_image.when_pressed = show_img
btn_video.when_pressed = show_vid

pause()
