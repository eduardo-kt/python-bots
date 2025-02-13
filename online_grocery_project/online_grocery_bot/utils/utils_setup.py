import os
import logging
import traceback
from botcity.web import WebBot, Browser, By
from botcity.plugins.csv import BotCSVPlugin
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

    lineno = traceback.extract_tb(err.__traceback__)[-1].lineno
    logging.error(f'{type(err).__name__}:{err} - Linha: {lineno}')


def web_bot_setup(URL: str) -> WebBot:
    """Instancia e configura o WebBot."""

    bot = WebBot()
    bot.browser = Browser.FIREFOX
    bot.headless = False
    bot.driver_path = GeckoDriverManager().install()
    bot.browse(URL)
    bot.driver.maximize_window()
    return bot


def login_community(bot: WebBot,
                    username: str,
                    password: str) -> None:
    """Realiza todo o processo de Community login no Automation Anywhere"""

    bot.find_element(utils_variables.XPATH_ACCEPT_COOKIES,
                     By.XPATH).click()
    bot.wait(3000)  # Firefox executava antes da hora
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


def csv_routine(bot: WebBot) -> list:
    """Executa as subrotinas de baixar, salvar e configurar arquivo de csv."""

    try:
        csv_download(bot)
        csv_transfer_to_folder()
        csvfile = csvfile_config_as_list()
    except Exception as err:
        custom_error_message(err=err)
    return csvfile


def csv_download(bot: WebBot):
    try:
        bot.find_element(selector="//a[@class='btn btn-success']",
                         by=By.XPATH).click()
        bot.wait(2000)
        logging.info("Sucesso em fazer download dos dados.")
    except Exception as err:
        custom_error_message(err=err)


def csv_transfer_to_folder():
    """Transfere file do local de download para a pasta desejada."""

    try:
        os.rename(
            src=utils_variables.DEPARTURE,
            dst=utils_variables.DESTINATION
        )
        logging.info("Sucesso em transferir dados para pasta archive.")
    except Exception as err:
        custom_error_message(err=err)


def csvfile_config_as_list() -> list:
    """Transforma aquivo .csv em python list."""

    bot_csv = BotCSVPlugin()
    bot_csv.read(utils_variables.DESTINATION)
    csv_as_list = bot_csv.as_list()
    return csv_as_list


def fill_url_with_data(data: list, bot: WebBot) -> None:
    """"Preencha os campos da página com os dados do csv.

        Parâmetros:
        data: dados do csv no formato de lista
        bot: instância da classe WebBot
    """

    for row in data:
        row = row[1].strip()
        bot.find_element(
            selector="input#myInput",
            by=By.CSS_SELECTOR
            ).send_keys(row)
        
        bot.find_element(
            "button#add_button",
            By.CSS_SELECTOR,
            ensure_clickable=True).click()

