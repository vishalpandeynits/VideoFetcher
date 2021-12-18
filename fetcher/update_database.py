from .models import Video
from .utils import format_data, search_videos

def update_new_videos():
    """
    Accepts data from search function, formats the required data,
    and bulk create into database.
    """
    data = search_videos()
    videos = format_data(data)
    
    # create a list of Video instances
    video_instances = [
        Video(**video) for video in videos
    ]
    try:
        # Bulk create records, skip if received any duplicate video(same video id).
        created = Video.objects.bulk_create(video_instances, ignore_conflicts = True)
        if created:
            print("New list of videos updated into database.")
            return created
    except Exception as ex:
        print("Error occured while inserting data.", ex)
    return None