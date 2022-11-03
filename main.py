import httpx, itertools, threading



class Botter:
    def __init__(self):
        self.threads = 100
        self.name = "mciem"
        self.proxies = itertools.cycle(open("proxies.txt", "r").read().splitlines())
        self.start()
    
    def bot(self):
        while True:
            try:
                proxy = next(self.proxies)
                client = httpx.Client(proxies = {
                    "http://": "http://" + str(proxy),
                    "https://": "http://" + str(proxy)}, timeout=10)
                
                client.headers = {
                    "accept": "*/*",
                    "accept-language": "en-US,en;q=0.5",
                    "content-type": "application/json",
                    "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\"",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-user": "?1",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
                }

                r = client.get('https://solo.to/' + self.name)

                if r.status_code == 200:
                    print("Success!")
                else:
                    print(r.status_code)
            except:
                pass
    
    def start(self):
        for i in range(self.threads):
            x = threading.Thread(target=self.bot)
            x.start()

Botter()
