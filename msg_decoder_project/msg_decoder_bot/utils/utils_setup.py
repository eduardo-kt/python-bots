import os
import logging
import traceback
from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager

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


def web_bot_setup(URL: str) -> WebBot:
    """Defina a estrutura da instância do WebBot"""

    bot = WebBot()
    bot.browser = Browser.CHROME
    bot.headless = False
    bot.driver_path = ChromeDriverManager().install()
    bot.browse(URL)
    bot.driver.maximize_window()
    return bot


def custom_error_message(err: Exception) -> None:
    """Defina o formato da exception que é enviada ao logfile."""

    lineno = traceback.extract_tb(err.__traceback__)[-1].lineno
    logging.error(f'{type(err).__name__}:{err} - Linha: {lineno}')


def login_community(bot: WebBot,
                    username: str,
                    password: str) -> None:
    """Realiza todo o processo de Community login no Automation Anywhere"""

    bot.find_element(utils_variables.XPATH_ACCEPT_COOKIES,
                     By.XPATH).click()

    bot.find_element(utils_variables.XPATH_COMMUNITY_BUTTON,
                     By.XPATH).click()

    bot.find_element(utils_variables.XPATH_NAME_LOGIN,
                     By.XPATH).send_keys(username)

    bot.find_element(utils_variables.XPATH_NEXT_BUTTON,
                     By.XPATH).click()
    bot.wait(2000)

    bot.paste(password)

    bot.find_element(utils_variables.XPATH_LOGIN_BUTTON,
                     By.XPATH).click()
    
    