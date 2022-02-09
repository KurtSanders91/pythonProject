import logging
import logging.config
import yaml
import sys

# my_formatter = logging.Formatter("%(asctime)s[%(levelname)s] %(filename)s:%(lineno)d: %(message)s")
#
# output_file_handler = logging.FileHandler("demo.log")
# output_file_handler.setFormatter(my_formatter)
#
# stdout_handler = logging.StreamHandler(sys.stdout)
# stdout_handler.setFormatter(my_formatter)
# stdout_handler.setLevel(logging.ERROR)
#
# log = logging.getLogger(__name__)
# log.setLevel(logging.DEBUG)
# log.addHandler(output_file_handler)
# log.addHandler(stdout_handler)
#
# log.debug("This is DEBUG")
# log.info("This is INFO")
# log.warning("This is WARNING")
# log.error("This is ERROR")
# log.fatal("This is FATAL")


with open(file="./logging_config.yaml", mode='r') as file:
    logging_yaml = yaml.load(stream=file, Loader=yaml.FullLoader)
    logging.config.dictConfig(config=logging_yaml)

logging.getLogger("telemetry").info("start")
logging.debug("This is DEBUG")
logging.info("This is INFO")
logging.warning("This is WARNING")
logging.error("This is ERROR")
logging.fatal("This is FATAL")
logging.getLogger("telemetry").info("end")