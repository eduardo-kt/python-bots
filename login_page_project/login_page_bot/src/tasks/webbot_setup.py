import sys
import logging
from botcity.web import WebBot, Browser
from webdriver_manager.firefox import GeckoDriverManager
from src.utils.customize_error import custom_error_message


def webbot_setup(URL: str) -> WebBot:
    """Instancia e configura o WebBot."""

    try:
        bot = WebBot()
        bot.browser = Browser.FIREFOX
        bot.headless = False
        bot.driver_path = GeckoDriverManager().install()
        bot.browse(URL)
        bot.driver.maximize_window()
        logging.info("Sucesso ao instanciar o bot.")
        return bot
    except Exception as err:
        logging.error("Erro ao instanciar o bot.")
        custom_error_message(err=err)
        sys.exit()
