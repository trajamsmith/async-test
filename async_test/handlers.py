import json
import asyncio
import time

from notebook.base.handlers import APIHandler
from notebook.utils import url_path_join
import tornado


class RouteHandler(APIHandler):
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server
    @tornado.web.authenticated
    async def get(self):
        start = time.time()
        await asyncio.sleep(10)
        end = time.time()

        print(f"Handler took {round(end - start, 3)} seconds to return.")
        self.finish(json.dumps({"data": "This is /async_test/get_example endpoint!"}))


def setup_handlers(web_app):
    host_pattern = ".*$"

    base_url = web_app.settings["base_url"]
    route_pattern = url_path_join(base_url, "async_test", "get_example")
    handlers = [(route_pattern, RouteHandler)]
    web_app.add_handlers(host_pattern, handlers)
