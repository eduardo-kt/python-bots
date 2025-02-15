from botcity.maestro import BotMaestroSDK
from src.utils.variables import URL_SOURCE
from src.utils.log_utils import loggin_startup
from src.tasks.webbot_setup import webbot_setup
from src.tasks.fill_credentials import fill_credentials
from src.tasks.maestro_tasks import maestro_closure, maestro_startup


BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():

    loggin_startup()

    maestro, execution = maestro_startup()

    bot = webbot_setup(URL=URL_SOURCE)

    # Implement here your logic...
    fill_credentials(bot=bot)

    maestro_closure(
        wait_time=3000,
        bot=bot,
        execution=execution,
        maestro=maestro,
    )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == "__main__":
    main()
