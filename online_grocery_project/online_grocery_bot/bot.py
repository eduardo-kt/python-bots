import os
import logging
from dotenv import load_dotenv
from botcity.core import DesktopBot
from botcity.maestro import BotMaestroSDK, AutomationTaskFinishStatus
from utils import utils_setup, utils_variables

load_dotenv()
username_aa = os.getenv('AA_CREDENTIAL_USERNAME')
password_aa = os.getenv('AA_CREDENTIAL_PASSWORD')

BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    # Inicia Log
    try:
        utils_setup.logfile_setup()
        logging.info("Início do processo.")
        logging.info("Sucesso ao iniciar logfile na pasta archive.")
    except Exception as err:
        print(f'{type(err).__name__}:{err}')

    # Configura Maestro
    try:
        maestro = BotMaestroSDK.from_sys_args()
        execution = maestro.get_execution()
        print(f"Task ID is: {execution.task_id}")
        print(f"Task Parameters are: {execution.parameters}")
        logging.info("Sucesso na configuração do Botcity Maestro.")
    except Exception as err:
        utils_setup.custom_error_message(err=err)

    # Instancia Bot
    try:
        webbot = utils_setup.web_bot_setup(
            URL=utils_variables.URL_SOURCE
        )
        logging.info("Sucesso ao instanciar o bot.")
    except Exception as err:
        utils_setup.custom_error_message(err=err)

    # Login em Area Community
    try:
        utils_setup.login_community(
            bot=webbot,
            username=username_aa,
            password=password_aa
        )
        logging.info(
            "Sucesso ao acessar a Área Community do Automation Anywhere."
        )
    except Exception as err:
        utils_setup.custom_error_message(err=err)

    # Download e preparo de csv
    try:
        csv_data_as_list = utils_setup.csv_routine(bot=webbot)
        logging.info("Download realizado.")
        logging.info("Sucesso no preparo dos dados.")
    except Exception as err:
        utils_setup.custom_error_message(err=err)

    # Iterar dados na URL
    try:
        utils_setup.fill_url_with_data(
            data=csv_data_as_list,
            bot=webbot
        )
        logging.info("Sucesso ao transmitir dados para a URL.")
    except Exception as err:
        utils_setup.custom_error_message(err=err)
    
    # Finalizar processo na URL
    

    webbot.wait(3000)
    webbot.stop_browser()
    maestro.finish_task(
        task_id=execution.task_id,
        status=AutomationTaskFinishStatus.SUCCESS,
        message="Task Finished OK.",
        total_items=0,
        processed_items=0,
        failed_items=0
    )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
