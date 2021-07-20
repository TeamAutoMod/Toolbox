from typing import Callable



def silent(function: Callable, *args, **kwargs):
    try:
        function(*args, **kwargs)
    except Exception:
        pass


async def async_silent(function: Callable, *args, **kwargs):
    try:
        await function(*args, **kwargs)
    except Exception:
        pass
