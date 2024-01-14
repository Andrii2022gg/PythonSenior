import logging

logging.basicConfig(level=logging.INFO,
                    filename="logs.log",
                    filemode="w",
                    format="My logging: %(levelname)s: %(asctime)s: %(message)s")

try:
    print(5 / 0)
except Exception:
    logging.exception("Division by zero Exception")

logging.debug("DEBUG")
logging.info("INFO")
logging.warning("WARNING")
logging.error("ERROR")
logging.critical("CRITICAL")