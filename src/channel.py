import json
import os

from googleapiclient.discovery import build

import isodate

class Channel:
    """Класс для ютуб-канала"""

    api_key = "AIzaSyDPB_Ed33-S5rIPo_Aw8cPoMwkvYX95bM4"  # сейчас я не могу установить API KEY в переменные окружения из-за компьютера, но принцип я поняла
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        request = self.youtube.channels().list(part="snippet,statistics", id=self.channel_id)

        response = request.execute()
        channel_info = response.get("items")[0] if "items" in response else {}

        # return json.dumps(channel_info, indent=2, ensure_ascii=False)
        print(json.dumps(channel_info, indent=2, ensure_ascii=False))
