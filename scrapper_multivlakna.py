#----------------------scrapper pomocou vlakien----------------
import threading
import urllib.request
import time

def download_site(url):
    with urllib.request.urlopen(url) as response:
        print(f"Stiahnutie {url}: {len(response.read())} bytov")


sites = [
    "http://www.example.com",
    "http://www.example.org",
    "http://www.example.net",
]

threads = []
start_time = time.time()


for url in sites:
    thread = threading.Thread(target=download_site, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

duration = time.time() - start_time
print(f"Stiahnute {len(sites)} stranok za {duration}  sekund")

