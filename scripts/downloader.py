import re
import requests
import os
import glob


def download(url):
    files = glob.glob('chunks/*')
    for file in files:
        os.remove(file)

    i = int(re.search(r':(.*)\}', re.search(r'\$\{num:(\d)+\}', url).group()).group()[1:-1])
    while True:
        chunk_url = re.sub(r'\$\{num:(\d)+\}', str(i), url)
        print('Dowloading chunck ' + str(i) + '...')
        response = requests.get(chunk_url)
        if response.status_code != 200:
            print('End of stream was reached or an error occurred.')
            break
        open('chunks/chunk_' + str(i) + '.ts', 'wb').write(response.content)
        i += 1
