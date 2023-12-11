import logging
from time import sleep

logger = logging.getLogger(__name__)
formatter = logging.Formatter("%(asctime)s - [%(levelname)8s] %(name)s.%(lineno)d --- %(message)s")
logger.setLevel(logging.INFO)

def task(env, duration=1, size=1):
    """
    sleeps `duration`  second and returns `size` times "x", used to test timeouts and large outputs.
    also does progressive logging
    """
    # sleep duration seconds
    step = int(duration / 10)

    for i in range(0, step):
        logger.info(f"{i * 10}s")
        sleep(10)

    logger.info(f"sleep for {duration}s - DONE")
    # return size times "x"
    return "x" * size
