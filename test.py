from pprint import pprint
import requests

Yandex_Token =''



class YaUploader:

    host = ' https://cloud-api.yandex.net:443'
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self):
        url = f'{self.host}/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        pprint(response.json())

    def _get_upload_link(self, path):
        url = f'{self.host}/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': path, 'overwrite': True}
        response = requests.get(url, headers=headers, params=params)
        pprint(response.json())
        return response.json().get('href')

    def upload(self, path, file_name):
        upload_link = self._get_upload_link(path)
        headers = self.get_headers()
        response = requests.put(upload_link, data=open(file_name, 'rb'), headers=headers)
        # response.raise_for_status()
        # if response.status_cod == 201 :
        #     print('Succses')

if __name__ == '__main__':
    uploader = YaUploader(Yandex_Token)
    uploader.upload('/test.txt', 'Hello_World.txt')


url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'

resp = requests.get(url)
heroes = resp.json()
heroes_list = ['Hulk', 'Captain America', 'Thanos']
heroes_dict = {}
for l in heroes:
    if l['name'] in heroes_list:
        heroes_dict[l['name']] = (l['powerstats']['intelligence'])
print(heroes_dict)
print(max(heroes_dict, key=heroes_dict.get))



