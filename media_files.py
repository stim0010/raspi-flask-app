import os

#append list of files names from the images folder
def get_images():
    image_list = []
    for file in os.listdir('static/media/images'):
        image_list.append(file)
    return image_list

#append list of files names from the videos folder
def get_videos():
    video_list = []
    for file in os.listdir('static/media/videos'):
        video_list.append(file)
    return video_list