import argparse
import asyncio
import aiohttp
import random

def rand_str():
  r = lambda: random.randint(0,255)
  s = 'user-%02X%02X%02X' % (r(),r(),r())
  return s

async def make_requests(args, cli):
  add_name = f'{args.host}/names/add'
  list_names = f'{args.host}/names/list'
  delete_names = f'{args.host}/names/delete'

  for i in range(0, 3):
    url = f'{add_name}/{rand_str()}'
    async with cli.post(url) as res:
      if res.status == 200:
        data = await res.json()
        print(data)
        if data['index'] > 20:
          async with cli.post(delete_names) as res2:
            if res2.status == 200:
              print(f'Names deleted')
    await asyncio.sleep(1);

  async with cli.get(list_names) as res:
    print(res.status)
    print(await res.text())

async def main(args):
  async with aiohttp.ClientSession() as cli:
    while True:
      try:
        await make_requests(args, cli)
      except Exception as e:
        print(f'ERROR {e.errno}: {e.strerror}')
      await asyncio.sleep(3)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--host', type=str, default='http://localhost:8088')
  args = parser.parse_args()
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main(args))
