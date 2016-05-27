import logging

request_logger = logging.getLogger('api.request.logger')

class LoggingMiddleware(object):
    _initial_http_body = None

    def process_request(self, request):
        self._initial_http_body = request.body

    def process_response(self, request, response):
        if request.method == 'GET':
            request_logger.log(logging.DEBUG,
                    "GET: {}. cookies: {}. body: {} response code: {}. "
                    "cookies: {}"
                    "response "
                    "content: {}"
                    .format(request.GET, request.COOKIES, self._initial_http_body,
                            response.status_code,
                            response.cookies,
                            response))

        if request.method == 'POST':
            request_logger.log(logging.DEBUG,
                    "POST: {}. body: {} response code: {}. "
                    "response "
                    "cookies: {}"
                    "content: {}"
                    .format(request.POST, self._initial_http_body,
                            response.status_code,
                            response.cookies,
                            response))

        return response
