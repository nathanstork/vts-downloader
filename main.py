from scripts import downloader, merger


def main():
    urls = [
        'https://streaming10.ur.se/urplay/_definst_/mp4:se/207000-207999/207811-4.mp4/media_${num:0}.ts',  # Example URL
        'https://streaming10.ur.se/urplay/_definst_/mp4:se/207000-207999/207810-5.mp4/media_${num:0}.ts',  # Example URL
        'https://streaming10.ur.se/urplay/_definst_/mp4:se/207000-207999/207813-8.mp4/media_${num:0}.ts'  # Example URL
    ]

    for url in urls:
        downloader.download(url)
        merger.merge()

    downloader.clear_chunks()


if __name__ == '__main__':
    main()
