from apscheduler.schedulers.background import BackgroundScheduler
from . import utils

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(utils.update_new_videos, 'interval', seconds=10)
    scheduler.start()