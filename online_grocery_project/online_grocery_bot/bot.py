import logging
from botcity.core import DesktopBot
from botcity.web import WebBot, Browser, By
from botcity.maestro import BotMaestroSDK
from utils import utils_setup, utils_variables

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

    desktop_bot = DesktopBot()

    # Execute operations with the DesktopBot as desired
    # desktop_bot.control_a()
    # desktop_bot.control_c()
    # value = desktop_bot.get_clipboard()

    # Implement here your logic...
    ...

    # Wait 3 seconds before closing
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
