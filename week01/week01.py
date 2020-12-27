import logging
from datetime import datetime
import os

now_time = datetime.strftime(datetime.now(), "%Y%m%d")
log_dir = "/var/log/python-%s" % now_time
log_file = log_dir + "/week01.log"

if  not os.path.exists(log_dir):
    print(log_dir + "not exists")
    os.makedirs(log_dir)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d] %(message)s',
    filename=log_file,
)


def main():
    logging.info("execute main.")
    print("hello python, %s" % __name__)


if __name__ == "__main__":
    main()
print(log_file)
print(os.path.abspath(log_file))
print(os.path.basename(log_file))