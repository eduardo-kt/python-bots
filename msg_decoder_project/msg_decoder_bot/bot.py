import logging
import subprocess
from botcity.web import WebBot, Browser, By
from botcity.maestro import BotMaestroSDK

from utils import utils_setup

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
    except Exception as err:
        utils_setup.custom_error_message(err=err)
    
    # Fecha navegador
    try:
        subprocess.run(["taskkill", "/f", "/im", "firefox.exe"])
        logging.info("Sucesso em fechar app Firefox.")
    except Exception as err:
        setup_utils.custom_error_message(err=err)    
    
    # Instancia bot
    try:
        bot = utils_setup.web_bot_setup()
    except Exception as err:
        setup_utils.custom_error_message(err=err)
    

    # Implement here your logic...
    ...

    # Wait 3 seconds before closing
    bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK.",
    #     total_items=0,
    #     processed_items=0,
    #     failed_items=0
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
