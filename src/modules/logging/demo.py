import logging


logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Basic types of logs 
logging.debug("debug")
logging.critical("critical")
logging.info("info")
logging.error("error")
logging.warning("warning")

# You can log a VARIABLE as well
a = 22
logging.info(f" The value of the a : {a}")


# You can log a ERROR as well

try :
    1 / 0
except ZeroDivisionError as e:
    logging.error("Zero Division Error", exc_info=True)


# Logger Object

logger = logging.getLogger(__name__)


handler = logging.FileHandler("test.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("Test the custom logger")
