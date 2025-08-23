import asyncio
import aiohttp
import async_timeout
import ssl
import re

BASE_URL = "https://fumbbl.com/api/position/get/"
START_ID = 20001
END_ID = 30000
MAX_CONCURRENT = 5
DELAY_BETWEEN_REQUESTS = 0.5  # seconds

sem = asyncio.Semaphore(MAX_CONCURRENT)

def sanitize_filename(text):
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', text)

async def fetch(session, id_):
    url = f"{BASE_URL}{id_}"
    async with sem:
        try:
            async with async_timeout.timeout(10):
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()

                        # skip if data only contains 'specialRules' as an empty list
                        if list(data.keys()) == ["specialRules"] and not data["specialRules"]:
                            print(f"ID {id_}: Empty data (only specialRules)")
                            return

                        title = data.get("title", f"no_title_{id_}")
                        race = data.get("race", "unknown_race")
                        filename = f"{sanitize_filename(race)}_{sanitize_filename(title)}.txt"

                        with open(filename, "w", encoding="utf-8") as f:
                            f.write(str(data))

                        print(f"Saved ID {id_} to {filename}")
                    elif response.status == 404:
                        print(f"ID {id_}: Not Found")
                    else:
                        print(f"ID {id_}: Status {response.status}")
        except Exception as e:
            print(f"ID {id_}: Error {e}")
        await asyncio.sleep(DELAY_BETWEEN_REQUESTS)

async def main():
    ssl_context = ssl.create_default_context()
    ssl_context.set_ciphers("DEFAULT@SECLEVEL=1")  # Helps with picky TLS servers

    connector = aiohttp.TCPConnector(ssl=ssl_context)
    headers = {"User-Agent": "Mozilla/5.0"}

    async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
        tasks = [fetch(session, i) for i in range(START_ID, END_ID + 1)]
        await asyncio.gather(*tasks)

asyncio.run(main())
