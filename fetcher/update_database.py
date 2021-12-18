from .models import Video
from .utils import format_data, search_videos

def update_new_videos():
    data = search_videos()
    videos = format_data(data)
    video_instances = [
        Video(**video) for video in videos
    ]
    try:
        created = Video.objects.bulk_create(video_instances, ignore_conflicts = True)
        if created:
            print("New list of videos updated into database")
    except Exception as ex:
        print("Error occured while inserting data.", ex)