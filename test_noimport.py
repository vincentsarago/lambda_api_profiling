import pstats
import cProfile

from APP_FastAPI.handler import handler as FastAPI_handler
from APP_lambda_proxy.handler import handler as LambdaProxy_handler


event = {
    "path": "/ping",
    "httpMethod": "GET",
    "headers": None,
    "queryStringParameters": {},
    "requestContext": {},
    "multiValueQueryStringParameters": {},
}


def profileit(func):
    """Profiling."""

    def wrapper(*args, **kwargs):
        prof = cProfile.Profile()
        retval = prof.runcall(func, *args, **kwargs)
        ps = pstats.Stats(prof)
        ps.strip_dirs().sort_stats("time").print_stats(10)
        return retval

    return wrapper


@profileit
def mainFast():
    FastAPI_handler(event, {})


@profileit
def mainProxy():
    LambdaProxy_handler(event, {})


if __name__ == '__main__':
    print("FastAPI + Mangum")
    mainFast()
    print()
    print("LambdaProxy")
    mainProxy()
