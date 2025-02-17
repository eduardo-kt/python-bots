from botcity.maestro import BotMaestroSDK

from src.utils.log_utils import setup_logging
from src.tasks.maestro_tasks import finalize_maestro, initialize_maestro

BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():

    setup_logging()

    maestro, execution = initialize_maestro()

    bot = WebBot()

    bot.headless = False

    # bot.browser = Browser.FIREFOX

    # bot.driver_path = "<path to your WebDriver binary>"

    # Opens the BotCity website.
    bot.browse("https://www.botcity.dev")

    # Wait 3 seconds before closing
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
