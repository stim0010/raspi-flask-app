from gpiozero import Button
from signal import pause

#assign input variables to gpio pins
btn_image = Button(12)
btn_video = Button(13)

#define the functions to be called when the button is pressed
def show_vid():
    print("Video")

def show_img():
    print("Image")

#call the functions when the button is pressed
btn_image.when_pressed = show_img
btn_video.when_pressed = show_vid

#wait for the events to happen
pause()
