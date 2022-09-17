from scripts import downloader, merger


def main():
    url = 'https://streaming10.ur.se/urplay/_definst_/mp4:se/207000-207999/207811-4.mp4/media_${num:0}.ts'  # Example URL

    downloader.download(url)
    merger.merge()


if __name__ == '__main__':
    main()
