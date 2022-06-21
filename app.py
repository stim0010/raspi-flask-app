from flask import Flask, render_template
import datetime
import os
import media_files

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

@app.route('/video')
def video():
    video_name = media_files.get_videos()
    return render_template('video.html', video_name=video_name)

@app.route('/image')
def image():
  image_name = media_files.get_images() 
  return render_template('image.html', image_name=image_name)

# @app.route('/events')
# def events():
  ##listen for events --> if image is clicked, show image --> if video is clicked, show video


if __name__ == "__main__":
   app.run()