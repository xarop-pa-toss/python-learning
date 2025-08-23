import asyncio
import aiohttp
import async_timeout
import ssl
import re
import json

ROSTER_IDS = [
    4956, 4957, 4958, 4959, 4960, 4961, 4962, 4963, 4964, 4965, 4966, 4969,
    4970, 4971, 4972, 4974, 4975, 4976, 4977, 4978, 4979, 5141, 5142, 5143,
    5144, 5145, 5146, 5160, 5916, 6217, 7544
]

BASE_URL = "https://fumbbl.com/api/roster/get/"
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
                    text = await response.text()

                    if "can't parse JSON" in text or "Unsupported ruleset" in text:
                        print(f"ID {id_}: Skipped due to unsupported response")
                        return

                    if response.status == 200:
                        try:
                            data = await response.json()
                        except Exception:
                            print(f"ID {id_}: Failed to parse JSON")
                            return


                        name = data.get("name", f"no_name_{id_}")
                        filename = f"BB2020 - {sanitize_filename(name)}.json"

                        with open(filename, "w", encoding="utf-8") as f:
                            json.dump(data, f, indent=2)

                        print(f"Saved ID {id_} to {filename}")
                    else:
                        print(f"ID {id_}: Status {response.status}")
        except Exception as e:
            print(f"ID {id_}: Error {e}")
        await asyncio.sleep(DELAY_BETWEEN_REQUESTS)

async def main():
    ssl_context = ssl.create_default_context()
    ssl_context.set_ciphers("DEFAULT@SECLEVEL=1")

    connector = aiohttp.TCPConnector(ssl=ssl_context)
    headers = {"User-Agent": "Mozilla/5.0"}

    async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
        tasks = [fetch(session, roster_id) for roster_id in ROSTER_IDS]
        await asyncio.gather(*tasks)

asyncio.run(main())
