import pstats
import cProfile


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
    from APP_FastAPI.handler import handler as FastAPI_handler
    FastAPI_handler(event, {})


@profileit
def mainProxy():
    from APP_lambda_proxy.handler import handler as LambdaProxy_handler
    LambdaProxy_handler(event, {})


if __name__ == '__main__':
    print("FastAPI + Mangum")
    mainFast()
    print()
    print("LambdaProxy")
    mainProxy()
