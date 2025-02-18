from botcity.maestro import BotMaestroSDK

from src.utils.log_utils import setup_logging
from src.utils.variables import URL_SOURCE
from src.tasks.setup_webbot import setup_webbot
from src.tasks.move_tasks import move_block
from src.tasks.maestro_tasks import finalize_maestro, initialize_maestro

BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():

    setup_logging()

    maestro, execution = initialize_maestro()

    bot = setup_webbot(URL=URL_SOURCE)

    move_block(bot=bot)

    finalize_maestro(
        wait_time=3000,
        bot=bot,
        execution=execution,
        maestro=maestro,
    )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == "__main__":
    main()
