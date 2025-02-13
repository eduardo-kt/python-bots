import os
import logging
from utils import utils_variables


def logfile_setup() -> None:
    """Defina a estrutura de apresentação dos logs"""

    os.environ['WDM_LOG'] = str(logging.NOTSET)
    log_dir = "archive"
    log_file = os.path.join(
        log_dir,
        f"{utils_variables.LOGFILE_KEY_NAME}_logfile.log"
    )

    logging.basicConfig(
        level=logging.INFO,
        filename=log_file,
        filemode="w",
        format="%(asctime)s %(levelname)s, linha %(lineno)d, %(message)s",
        encoding='utf-8',
    )
