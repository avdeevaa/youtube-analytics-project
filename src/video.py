import json
import os

from googleapiclient.discovery import build

import isodate

class Video:
    """класс для видео"""

    api_key: str = os.getenv('API_YOUTUBE')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        self.id_video = video_id
        videos_response = Video.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        self.videos_response = videos_response

        json_load_from_api = json.dumps(self.videos_response, indent=2, ensure_ascii=False)
        video_response = json.loads(json_load_from_api)

        self.video_title = video_response['items'][0]['snippet']['title'] # название видео
        self.video_url = video_response['items'][0]['snippet']['thumbnails']['default']['url']# ссылка на видео
        self.view_count = video_response['items'][0]['statistics']['viewCount'] # количество просмотров
        self.like_count = video_response['items'][0]['statistics']['likeCount'] # количество лайков

    def __str__(self):
        return self.video_title

class PLVideo(Video):
    """класс для плейлиста"""

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

        playlist_videos = PLVideo.youtube.playlistItems().list(playlistId=playlist_id,
                                               part='contentDetails',
                                               maxResults=50,
                                               ).execute()
        self.playlist_videos = playlist_videos



