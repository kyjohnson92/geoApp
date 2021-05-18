from asyncio.tasks import sleep
from aiohttp import web
from geo import GeoLocator

routes = web.RouteTableDef()


@routes.get('/{location}')
async def location(request):
    location = request.match_info['location']
    data = request.query

    getInfo = GeoLocator()
    print(data)
    return web.json_response(getInfo.GeoJson(location))

app = web.Application()
app.add_routes(routes)

web.run_app(app, host="localhost", port=8000)
