import os
import logging
import traceback
from botcity.web import WebBot, Browser
from webdriver_manager.firefox import GeckoDriverManager
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


def custom_error_message(err: Exception) -> None:
    """Defina o formato da exception que é enviada ao logfile."""

    lineno = traceback.extract_tb(err.__traceback___)[-1].lineno
    logging.error(f'{type(err).__name__}:{err} - Linha: {lineno}')


def web_bot_setup(URL: str) -> WebBot:
    """Instancia e configura o WebBot."""

    bot = WebBot()
    bot.browser = Browser.FIREFOX
    bot.headless = False
    bot.driver_path = GeckoDriverManager().install()
    bot.driver.maximize_window()
    return bot
