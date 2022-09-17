import re
import os
import shutil
from datetime import datetime


def merge():
    cwd = os.getcwd()
    chunks_dir = 'chunks'

    ts_files = []
    for ts_file in os.listdir(f'{cwd}/{chunks_dir}'):
        ts_files.append(ts_file)
    ts_files.sort(key=lambda f: int(re.sub('\D', '', f)))

    with open('output/merged_' + datetime.now().strftime('%m-%d-%Y_%H-%M-%S') + '.ts', 'wb') as merged:
        for ts_file in ts_files:
            with open(f'{cwd}/{chunks_dir}/{ts_file}', 'rb') as mergefile:
                shutil.copyfileobj(mergefile, merged)
