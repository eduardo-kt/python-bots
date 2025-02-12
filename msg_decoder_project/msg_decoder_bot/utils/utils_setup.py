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


def translate_and_return_string(bot: WebBot) -> None:
    """Transfere uma string entre fonte e tradutor
    e retorna texto traduzido."""

    bulgarian_string = bot.find_element(
        "p.lead.mt-2+h2",
        By.CSS_SELECTOR
    ).text
    bulgarian_string = bulgarian_string.replace("Text to Decode: ", "")
    logging.info(f"Sucesso ao capturar string:{bulgarian_string}")
    bot.create_tab(utils_variables.URL_TRADUTOR)
    opened_tabs = bot.get_tabs()
    tab_tradutor = opened_tabs[1]
    tab_bulgarian = opened_tabs[0]
    bot.activate_tab(tab_tradutor)
    logging.info("Sucesso ao abrir página do tradutor.")
    bot.find_element(
        "textarea.p-2",
        By.CSS_SELECTOR
    ).send_keys(bulgarian_string)
    while True:
        translate_string = bot.find_element(
            "div.h-full",
            By.CSS_SELECTOR
        ).text
        if translate_string:
            logging.info(f"Sucesso ao traduzir string: {translate_string}")
            break
    bot.activate_tab(tab_bulgarian)
    bot.find_element(
        "input#message_input",
        By.CSS_SELECTOR
    ).send_keys(translate_string)


def finish_and_screenshot_process(bot: WebBot) -> None:
    """Finaliza processo e salva tela em screenshot."""

    bot.find_element("a.btn", By.CSS_SELECTOR).click()
    bot.wait_for_element_visibility(
        bot.find_element("div.modal.fade.show", By.CSS_SELECTOR)
    )
    bot.get_screenshot(
        utils_variables.IMAGE_FILEPATH
    )
