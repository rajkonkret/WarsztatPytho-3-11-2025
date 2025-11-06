import asyncio
import aiohttp
import time


async def fetch(url, session, index):
    async with session.get(url, ssl=False) as response:
        text = await response.text()
        print(f"Text: {text}")


async def measure_aiohttp():
    url = "https://api.nbp.pl/api/exchangerates/rates/a/usd/"

    tasks = []
    overall_start_time = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        for i in range(100):
            tasks.append(fetch(url, session, i + 1))

        statuses = await asyncio.gather(*tasks)

    overall_elapsed_time = time.perf_counter() - overall_start_time
    print(f"Overall time for request: {overall_elapsed_time}")
    return statuses


# uruchomienie metod asynchronicznej
asyncio.run(measure_aiohttp())
# Overall time for request: 0.33878999995067716
