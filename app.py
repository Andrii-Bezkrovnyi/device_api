from aiohttp import web
from db_setup import db_setup
from routes import setup_routes

db_setup()
app = web.Application()
setup_routes(app)

if __name__ == '__main__':
    web.run_app(app, port=8080)
