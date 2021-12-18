# Backend Assignment - Github Externship
* [Video Fetcher](https://videofetcher.herokuapp.com/) <br>
* [Video Demo](https://www.youtube.com/watch?v=spMKHP5jT7I)

## Project Goal
To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## Requirements
1. Server should call the YouTube API continuously in background with some interval for fetching the latest videos for a predefined search query and should store the data of videos in a database with proper indexes.
2. A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
3. It should be scalable and optimised.

## Technologies used
1. Django
2. Django Rest framework
3. Sqlite3(Database)
4. Apscheduler

## Superuser Credentials
```
url: /admin
username: root
password: root
```
## How to run this project ?

* Clone the repository using

```bash
    https://github.com/vishalpandeyvip/VideoFetcher.git
```

* Install requirements using pip. Please make sure that you are in project's root directory.

```bash
pip3 install -r requirements.txt
```
* Generate your API keys from google as many as you want and put them into `API_KEYS` list which is in file `keys.py` located in `videofetcher` folder.
* Run migration commands using
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

* Run this command to test if any of your provided API keys are up and running
```bash
python3 manage.py test
```

* Runserver
```bash
python3 manage.py runserver
```

## Routes
[GET] `api/`: It returns a paginated response that contains the video id, title, description, channel name, publication date, and thumbnail URL of the video.
Sample Response
```
{
    "count": 1400,
    "next": "http://127.0.0.1:8000/api/?page=2",
    "previous": null,
    "results": [
        {
            "video_id": "U1l98JQ9rCg",
            "title": "How boorish treatment of Kohli by Ganguly’s BCCI takes Indian cricket back to an inglorious past",
            "description": "ViratKohli #BCCI #NationalInterest Ganguly is BCCI chief, Dravid is coach, Laxman heads NCA. And Kohli, all-conquering (in ...",
            "channel": "ThePrint",
            "published_on": "2021-12-18T11:06:50Z",
            "thumbnail_url": "https://i.ytimg.com/vi/U1l98JQ9rCg/default.jpg"
        },
        {
            "video_id": "GP1wthPMxA4",
            "title": "Omicron Update: दुनिया को शिकंजे में ले रहा है Omicron, Britain की हालत खराब | Latest News",
            "description": "Omicron Update: Omicron का संक्रमण बढ़ रहा है. इसकी मार पूरी दुनिया झेल रही है. ब्रिटेन में हर दिन ...",
            "channel": "Aaj Tak",
            "published_on": "2021-12-18T10:54:03Z",
            "thumbnail_url": "https://i.ytimg.com/vi/GP1wthPMxA4/default.jpg"
        },
    ]
}
```
[GET] `/dashboard`: Its response is same as the above-mentioned API. But in this API, filters and orderings are implemented so that users can filter out the videos on basis of the youtube channel name, video title, and description.
![Dashboard Image](https://github.com/vishalpandeyvip/VideoFetcher/blob/main/screenshots/dashboard.png)

Sample Response 
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 8620,
    "next": "http://127.0.0.1:8000/dashboard/?ordering=-published_on&page=2",
    "previous": null,
    "results": [
        {
            "video_id": "G4wBCkMdmMk",
            "title": "Moscow demands NATO pulls back as fears of Russia invading Ukraine rise",
            "description": "Moscow wants NATO to pledge that former Soviet states will never join the bloc and that its forces will pull back from Russia's ...",
            "channel": "euronews",
            "published_on": "2021-12-18T12:02:21Z",
            "thumbnail_url": "https://i.ytimg.com/vi/G4wBCkMdmMk/default.jpg"
        },
        {
            "video_id": "G4wBCkMdmMk",
            "title": "Moscow demands NATO pulls back as fears of Russia invading Ukraine rise",
            "description": "Moscow wants NATO to pledge that former Soviet states will never join the bloc and that its forces will pull back from Russia's ...",
            "channel": "euronews",
            "published_on": "2021-12-18T12:02:21Z",
            "thumbnail_url": "https://i.ytimg.com/vi/G4wBCkMdmMk/default.jpg"
        },
    ]
}
```

[GET] `/`: A simple youtube clone page that has a list of videos. Search box and paginations are also implemented to narrow down the query results.
![Alt text](https://github.com/vishalpandeyvip/VideoFetcher/blob/main/screenshots/home.png)
## License
[MIT](https://choosealicense.com/licenses/mit/)