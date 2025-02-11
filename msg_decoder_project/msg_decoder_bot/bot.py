import os
import logging
import subprocess
from dotenv import load_dotenv
from botcity.web import By
from botcity.maestro import BotMaestroSDK, AutomationTaskFinishStatus
from utils import utils_setup, utils_variables

# Desligar os logs do webdriver_manager
os.environ['WDM_LOG'] = str(logging.NOTSET)

load_dotenv()
username_aa = os.getenv('AA_CREDENTIAL_USERNAME')
password_aa = os.getenv('AA_CREDENTIAL_PASSWORD')
login_target = os.getenv('TEST_CREDENTIAL_USERNAME')
password_target = os.getenv('TEST_CREDENTIAL_PASSWORD')

BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    # Inicia log
    try:
        utils_setup.logfile_setup()
        logging.info("Início do processo.")
        logging.info("Sucesso em iniciar Logfile na pasta archive.")
    except Exception as err:
        print(f'{type(err).__name__}:{err}')

    # Configura maestro
    try:
        maestro = BotMaestroSDK.from_sys_args()
        execution = maestro.get_execution()
        print(f"Task ID is: {execution.task_id}")
        print(f"Task Parameters are: {execution.parameters}")
        logging.info("Sucesso na configuração do BotCity Maestro.")
    except Exception as err:
        utils_setup.custom_error_message(err=err)
    
    # Fecha navegador
    # try:
    #     subprocess.run(["taskkill", "/f", "/im", "chrome.exe"])
    #     logging.info("Sucesso em fechar app Chrome.")
    # except Exception as err:
    #     utils_setup.custom_error_message(err=err)    
    
    # Instancia bot
    try:
        bot = utils_setup.web_bot_setup()
        logging.info("Área Community acessada.")
    except Exception as err:
        utils_setup.custom_error_message(err=err)
    
    # Login em Area Community
    try:
        utils_setup.login_community(bot=bot,
                                    username=username_aa,
                                    password=password_aa)
        logging.info("Área Community acessada.")
    except Exception as err:
        utils_setup.custom_error_message(err=err)
    
    bot.wait(5000)

    #bot.stop_browser()
    
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
