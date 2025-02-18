import sys
import logging
from botcity.web import WebBot, Browser
from webdriver_manager.chrome import ChromeDriverManager
from src.utils.customize_error import format_error_message


def setup_webbot(URL: str) -> WebBot:
    """
    Instancia e configugra o WebBot.

    Args:
        URL (str): URL da página que o bot irá operar.

    Return:
        WebBot: Objeto da classe WebBot.
    """

    try:
        bot = WebBot()
        bot.browser = Browser.CHROME
        bot.headless = False
        bot.driver_path = ChromeDriverManager().install()
        bot.browse(url=URL)
        logging.info("Sucesso ao instanciar o bot.")
        return bot
    except Exception as err:
        logging.error("Erro ao instanciar o bot.")
        format_error_message(err=err)
        sys.exit()
