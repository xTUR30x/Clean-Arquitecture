#Proxy Pattern

class VideoDownloader:

    def download(self, url: str) -> bool:
        print("Descargando video...")
        print("Video Descargado Exitosamente!")
        return True
    

class CachedVideoDownloader:

    def __init__(self) -> None:
        self.downloader = VideoDownloader()
        self.cache = {}

    def download(self, url: str) -> None:
        if url not in self.cache:
            self.cache[url] = self.downloader.download(url)
        else:
            print("El video ya ha sido descargado")
    

if __name__ == '__main__':
    proxy = CachedVideoDownloader()
    proxy.download("https://www.youtube.com/watch?v=dQw4w9WgX")
    proxy.download("https://www.youtube.com/watch?v=dQw4w9WgX")