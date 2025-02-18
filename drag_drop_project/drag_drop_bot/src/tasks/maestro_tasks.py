import sys
import logging
from botcity.web import WebBot
from botcity.maestro import (
    BotExecution,
    BotMaestroSDK,
    AutomationTaskFinishStatus,
)
from src.utils.customize_error import format_error_message


def initialize_maestro() -> tuple:
    """
    Inicializa o framework Botcity Maestro.

    Args: None.

    Return:
        tuple: Contém objeto BotMaestroSDK e informações do BotExecution.
    """
    try:
        maestro = BotMaestroSDK.from_sys_args()
        execution = maestro.get_execution()
        logging.info("Sucesso na inicialização do BotCity Maestro.")
        logging.info(f"Task ID is: {execution.task_id}")
        logging.info(f"Task Parameters are: {execution.parameters}")
        return maestro, execution
    except Exception as err:
        logging.error("Erro durante inicialização do BotCity Maestro.")
        format_error_message(err=err)
        sys.exit()


def finalize_maestro(
    wait_time: int,
    bot: WebBot,
    execution: BotExecution,
    maestro: BotMaestroSDK,
) -> None:
    """
    Encerra o framework BotCity Maestro.

    Args:
        wait_time (int): Espera por um tempo (em milisegundos)
        bot (WebBot): objeto da classe WebBot.
        execution (BotExecution): Objeto da classe BotExecution.
        maestro (BotMaestroSDK): Objeto da classe BotMaestroSDK.

    Return: None.
    """
    try:
        bot.wait(wait_time)
        bot.stop_browser()
        maestro.finish_task(
            task_id=execution.task_id,
            status=AutomationTaskFinishStatus.SUCCESS,
            message="Task Finished OK.",
            total_items=0,
            failed_items=0,
        )
    except Exception as err:
        print("Erro ao finalizar framework BotCity Maestro.")
        print(f"{type(err).__name__}: {err}")
