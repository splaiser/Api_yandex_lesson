import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            "Contens-Type": 'application/json',
            "Authorization": f'OAuth {self.token}'
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        href_dict = self._get_upload_link(disk_file_path=disk_file_path)
        href = href_dict.get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Выполненно")

    # def get_file_list(self):
    #     files_url = "https://cloud-api.yandex.net/v1/disk/resources/files"
    #     headers = self.get_headers()
    #     response = requests.get(files_url, headers=headers)
    #     return response.json()


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "netology/1.txt"  # Указать путь куда загружать файл
    token = ""  # Указать токен
    uploader = YaUploader(token)
    uploader.upload_file_to_disk(path_to_file, '1.txt')

