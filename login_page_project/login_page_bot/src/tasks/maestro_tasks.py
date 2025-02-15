import sys
import logging
from botcity.web import WebBot
from botcity.maestro import (
    BotExecution,
    BotMaestroSDK,
    AutomationTaskFinishStatus,
)
from src.utils.customize_error import custom_error_message


def maestro_startup():
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


def maestro_closure(
    wait_time: int,
    bot: WebBot,
    execution: BotExecution,
    maestro: BotMaestroSDK,
) -> None:
    """Encapsula os processos de encerramento do Maestro Botcity."""

    try:
        bot.wait(2000)
        bot.stop_browser()
        maestro.finish_task(
            task_id=execution.task_id,
            status=AutomationTaskFinishStatus.SUCCESS,
            message="Task Finished OK.",
            total_items=0,
            processed_items=0,
            failed_items=0,
        )
    except Exception as err:
        print("Erro ao finalizar botcity Maestro.")
        print(f"{type(err).__name__}:{err}")
