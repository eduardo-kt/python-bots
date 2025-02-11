import os
import logging
import traceback
from botcity.web import WebBot, Browser
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

from utils import utils_variables


def logfile_setup() -> None:
    """Defina a estrutura de apresentação dos logs"""

    os.environ['WDM_LOG'] = str(logging.NOTSET)
    log_dir = "archive"
    log_file = os.path.join(
        log_dir,
        f"logfile_{utils_variables.LOGFILE_KEY_NAME}.log"
    )

    logging.basicConfig(
        level=logging.INFO,
        filename=log_file,
        filemode="w",
        format="%(asctime)s %(levelname)s, linha %(lineno)d, %(message)s",
        encoding='utf-8',
    )


def web_bot_setup() -> WebBot:
    """Defina a estrutura da instância do WebBot"""

    bot = WebBot()
    bot.browser = Browser.CHROME
    bot.headless = False
    bot.driver_path = ChromeDriverManager().install()
    bot.browse(utils_variables.URL_SOURCE)    
    bot.driver.maximize_window()
    return bot


def custom_error_message(err):
    """Defina o formato da exception que é enviada ao logfile."""

    lineno = traceback.extract_tb(err.__traceback__)[-1].lineno
    logging.error(f'{type(err).__name__}:{err} - Linha: {lineno}')
