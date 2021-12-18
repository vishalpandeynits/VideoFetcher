from apscheduler.schedulers.background import BackgroundScheduler
from . import update_database

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_database.update_new_videos, 'interval', seconds=10)
    scheduler.start()