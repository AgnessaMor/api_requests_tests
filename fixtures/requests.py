from requests import Response
from requests.adapters import HTTPAdapter
from requests import Session as Session_api

# Transport Adapters let define a set of configurations per service interacting with request.  # noqa
# max_retries - number of repetitions request, if it falls with an error  # noqa
custom_adapter = HTTPAdapter(max_retries=3)
# Session for need to fine-tune control over how requests are being made
s = Session_api()


class Client:
    @staticmethod
    def request(method: str, url: str, **kwargs) -> Response:
        """
        Request method
        method: method for the new Request object: GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE. # noqa
        url – URL for the new Request object.
        **kwargs:
            params – (optional) Dictionary, list of tuples or bytes to send in the query string for the Request. # noqa
            json – (optional) A JSON serializable Python object to send in the body of the Request. # noqa
            headers – (optional) Dictionary of HTTP Headers to send with the Request. # noqa

        It’s a good practice to set connect timeouts to slightly larger than a multiple of 3, # noqa
        which is the default TCP packet retransmission window (https://www.hjp.at/doc/rfc/rfc2988.txt). # noqa
        """

        # Use `custom_adapter` for all requests to endpoints that start with this URL  # noqa
        s.mount(url, custom_adapter)
        return s.request(method, url, timeout=(3.05, 27), **kwargs)
