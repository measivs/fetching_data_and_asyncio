import asyncio, aiohttp, json, time

first_object = [True]

async def fetch_and_write_to_json(url, filename, session):
    async with session.get(url) as response:
        data = await response.json()

        with open(filename, 'a') as file:
            if not first_object[0]:
                file.write(',\n')
            json.dump(data, file, indent=4)
            first_object[0] = False


async def main():
    posts_amount = 77
    base_url = f"https://jsonplaceholder.typicode.com/posts/"
    filename = 'data.json'

    start_time = time.perf_counter()

    with open(filename, 'w') as file:
        file.write('[')

    async with aiohttp.ClientSession() as session:
        tasks = []
        for n in range(1, posts_amount+1):
            url = f'{base_url}{n}'
            task = fetch_and_write_to_json(url, filename, session)
            tasks.append(task)
        
        await asyncio.gather(*tasks)

    with open(filename, 'a') as file:
            file.write(']')

    end_time = time.perf_counter()
    print(end_time - start_time)

asyncio.run(main())
