from botcity.web import WebBot, Browser, By
from botcity.maestro import *

from src.utils.log_utils import setup_logging

BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():

    setup_logging()

    maestro = BotMaestroSDK.from_sys_args()

    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    bot.headless = False

    # bot.browser = Browser.FIREFOX

    # bot.driver_path = "<path to your WebDriver binary>"

    # Opens the BotCity website.
    bot.browse("https://www.botcity.dev")

    # Wait 3 seconds before closing
    bot.wait(3000)

    bot.stop_browser()

    maestro.finish_task(
        task_id=execution.task_id,
        status=AutomationTaskFinishStatus.SUCCESS,
        message="Task Finished OK.",
        total_items=0,
        processed_items=0,
        failed_items=0,
    )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == "__main__":
    main()
