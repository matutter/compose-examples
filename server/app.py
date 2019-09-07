from typing import List
from aiohttp import web
import argparse
import asyncio
import aiormq

async def on_start(app):
  print(f'App started...')

async def add_name(req):
  names = req.app.names
  name:str = req.match_info.get('name', None)
  if name is None:
    return web.Response(status=500)
  names.append(name)
  print(f'Added new name "{name}"')
  return web.json_response(data=dict(index=len(names)-1))

async def list_names(req):
  names = req.app.names
  print(f'Listing {len(names)} names')
  return web.json_response(data=names)

async def delete_names(req):
  names = req.app.names
  print(f'Deleting {len(names)} names')
  while names:
    names.pop()
  return web.json_response(data=names)

async def main(args):
  app = web.Application()
  setattr(app, 'names', [])
  app.add_routes([
    web.post('/names/add/{name}', add_name),
    web.post('/names/delete', delete_names),
    web.get('/names/list', list_names)
  ])
  app.on_startup.append(on_start)
  runner = web.AppRunner(app)
  await runner.setup()
  site = web.TCPSite(runner, port=args.port)
  await site.start()

  while True:
    await asyncio.sleep(5)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--port', type=int, default=8088)
  args = parser.parse_args()
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main(args))
