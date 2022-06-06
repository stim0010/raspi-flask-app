from flask import Flask, render_template
from gpiozero import Button
from signal import pause 
import datetime

##GPIO buttons
video_btn = Button(12)
image_btn = Button(13)

def show_vid():
    print("Video button pressed")

def show_img():
    print("Image button pressed")

video_btn.when_pressed = show_vid
image_btn.when_pressed = show_img

pause()

##Flask app
app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
      'title' : 'WELCOME',
      'time': timeString
      }
    return render_template('index.html', **templateData)

# trying to get the button to render_template

# @app.route('/video')
# def video():
#     return render_template('video.html')

# @app.route('/image')
# def image():
#     return render_template('image.html')


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)