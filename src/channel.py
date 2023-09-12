import json
import os

from googleapiclient.discovery import build

import isodate

class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('API_YOUTUBE')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        videos_response = Channel.youtube.channels().list(part='snippet,statistics', id=channel_id).execute()
        self.videos_response = videos_response

        json_load_from_api = json.dumps(self.videos_response, indent=2, ensure_ascii=False)
        video_response = json.loads(json_load_from_api)


        self.channel_id = video_response['items'][0]['id'] # id канала
        self.title = video_response['items'][0]['snippet']['title'] # название канала
        self.channel_description = video_response['items'][0]['snippet']['description'] # описание канала
        self.url = video_response['items'][0]['snippet']['customUrl'] # ссылка на канал
        self.channel_followers = video_response['items'][0]['statistics']['subscriberCount'] # количество подписчиков
        self.video_count = video_response['items'][0]['statistics']['videoCount'] # количество видео
        self.channel_views = video_response['items'][0]['statistics']['viewCount'] # общее количество просмотров

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """прибавление"""
        return int(self.channel_followers) + int(other.channel_followers)

    def __sub__(self, other):
        """вычитание"""
        return int(self.channel_followers) - int(other.channel_followers)

    def __mul__(self, other):
        """умножение"""
        return int(self.channel_followers) * int(other.channel_followers)

    def __truediv__(self, other):
        """деление"""
        return int(self.channel_followers) / int(other.channel_followers)

    def __lt__(self, other):
        """меньше"""
        return self.channel_followers < other.channel_followers

    def __le__(self, other):
        """меньше или равно"""
        return self.channel_followers <= other.channel_followers

    def __gt__(self, other):
        """больше"""
        return self.channel_followers > other.channel_followers

    def __ge__(self, other):
        """больше или равно"""
        return self.channel_followers >= other.channel_followers

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        request = self.youtube.channels().list(part="snippet,statistics", id=self.channel_id)

        response = request.execute()
        channel_info = response.get("items")[0] if "items" in response else {}

        # return json.dumps(channel_info, indent=2, ensure_ascii=False)
        print(json.dumps(channel_info, indent=2, ensure_ascii=False))


    @classmethod
    def get_service(cls):
        """возвращает объект для работы с YouTube API"""

        api_key: str = os.getenv('API_YOUTUBE')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube


    def to_json(self, name):
        """сохраняет в файл значения атрибутов экземпляра Channel"""
        json_load_from_api = json.dumps(self.videos_response, indent=2, ensure_ascii=False)
        video_response = json.loads(json_load_from_api)

        with open(name, 'w') as file:
            json.dump(video_response, file)