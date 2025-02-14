import os
import sys
import logging
import traceback
from botcity.web import WebBot, Browser, By
from botcity.maestro import BotMaestroSDK
from botcity.plugins.csv import BotCSVPlugin
from webdriver_manager.firefox import GeckoDriverManager
from utils import utils_variables


def logfile_setup() -> None:
    """Defina a estrutura de apresentação dos logs"""

    try:
        os.environ['WDM_LOG'] = str(logging.NOTSET)
        log_dir = "archive"
        os.makedirs(log_dir, exist_ok=True)
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
        logging.info("Início do processo.")
        logging.info("Sucesso ao iniciar logfile na pasta archive.")
    except Exception as err:
        print("Erro durante criação de arquivo de logs.")
        print(f'{type(err).__name__}:{err}')
        sys.exit()


def maestro_setup():
    """Encapsula as definições iniciais do framework Botcity."""

    try:
        maestro = BotMaestroSDK.from_sys_args()
        execution = maestro.get_execution()
        logging.info("Sucesso na configuração do Botcity Maestro.")
        logging.info(f"Task ID is: {execution.task_id}")
        logging.info(f"Task Parameters are: {execution.parameters}")
        return maestro, execution
    except Exception as err:
        logging.error("Erro durente definição do BotCity Maestro.")
        custom_error_message(err=err)
        sys.exit()


def custom_error_message(err: Exception) -> None:
    """Defina o formato da exception que é enviada ao logfile."""

    lineno = traceback.extract_tb(err.__traceback__)[-1].lineno
    logging.error(f'{type(err).__name__}:{err} - Linha: {lineno}')


def web_bot_setup(URL: str) -> WebBot:
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


def login_community(bot: WebBot,
                    username: str,
                    password: str) -> None:
    """Realiza todo o processo de Community login no Automation Anywhere"""

    try:
        bot.find_element(utils_variables.XPATH_ACCEPT_COOKIES,
                         By.XPATH).click()
        bot.wait(2000)  # Firefox executava antes da hora        
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
        logging.info(
            "Sucesso ao acessar a Área Community do Automation Anywhere."
        )
    except Exception as err:
        logging.error(
            "Erro ao fazer login na área community Automation Anywhere."
        )
        custom_error_message(err=err)
        sys.exit()


def csv_routine(bot: WebBot) -> list:
    """Executa as subrotinas de baixar, salvar e configurar arquivo de csv."""

    try:
        csv_download(bot)
        csv_transfer_to_folder()
        csvfile = csvfile_config_as_list()
        logging.info("Sucesso no preparo dos dados.")
        return csvfile
    except Exception as err:
        logging.error("Erro no preparo dos dados.")
        custom_error_message(err=err)
        sys.exit()    


def csv_download(bot: WebBot):
    """Faz o download do arquivo csv."""

    try:
        bot.find_element(selector="//a[@class='btn btn-success']",
                         by=By.XPATH).click()
        bot.wait(2000)
        logging.info("Sucesso em fazer download dos dados.")
    except Exception as err:
        logging.error("Erro ao fazer o download dos dados.")
        custom_error_message(err=err)
        sys.exit()


def csv_transfer_to_folder():
    """Transfere file do local de download para a pasta desejada."""

    try:
        os.rename(
            src=utils_variables.DEPARTURE,
            dst=utils_variables.DESTINATION
        )
        logging.info("Sucesso em transferir arquivo para pasta archive.")
    except Exception as err:
        logging.error("Erro ao transferir arquivo para pasta archive.")
        custom_error_message(err=err)
        sys.exit()


def csvfile_config_as_list() -> list:
    """Transforma aquivo .csv em python list."""

    try:
        bot_csv = BotCSVPlugin()
        bot_csv.read(utils_variables.DESTINATION)
        csv_as_list = bot_csv.as_list()
        logging.info("Sucesso na conversão de dados para formato python list.")
        return csv_as_list
    except Exception as err:
        logging.error("Erro na conversão de dados para formato python list.")
        custom_error_message(err=err)
        sys.exit()    


def fill_url_with_data(data: list, bot: WebBot) -> None:
    """Preencha os campos da página com os dados do csv.

        Parâmetros:
        data: dados do csv no formato de lista
        bot: instância da classe WebBot
    """
    try:
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
        logging.info("Sucesso no preenchimento dos dados na URL.")        
    except Exception as err:
        logging.error("Erro no preenchimento dos dados na URL.")
        custom_error_message(err=err)
        sys.exit()   


def close_process(bot: WebBot) -> None:
    """Executa subrotinas para encerrar o processo."""
    
    try:
        submit_order(bot=bot)
        save_screen(bot=bot)
        logging.info("Fim do processo.")
    except Exception as err:
        logging.error("Erro ao finalizar processo.")
        custom_error_message(err=err)
        sys.exit() 


def submit_order(bot: WebBot) -> None:
    """Confirma checagens no site para submeter formulário."""

    try:
        bot.find_element("input#agreeToTermsYes", By.CSS_SELECTOR).click()
        bot.find_element("button#submit_button", By.CSS_SELECTOR).click()
        logging.info("Checagens realizadas com sucesso.")
    except Exception as err:
        logging.error("Erro ao realizar checagens.")
        custom_error_message(err=err)
        raise 


def save_screen(bot: WebBot):
    """Salva a tela do final do processo em um arquivo."""

    try:
        bot.wait_for_element_visibility(
            bot.find_element("div.modal.fade.show", By.CSS_SELECTOR)
        )
        bot.get_screenshot(
            utils_variables.IMAGE_FILEPATH
        )
        logging.info("Tela final salva em imagem na pasta archive.")        
    except Exception as err:
        logging.error("Erro ao salvar tela final.")
        custom_error_message(err=err)
        raise 
