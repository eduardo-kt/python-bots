import sys
import logging
from collections import namedtuple
from botcity.web import WebBot, By
from selenium.webdriver.common.action_chains import ActionChains
from src.utils.customize_error import format_error_message

Position = namedtuple("Position", ["x", "y"])


def move_block(bot: WebBot) -> None:
    """
    Move um objeto html de uma posição para outra.

    Args:
        bot (WebBot): Instancia da classe WebBot.

    Return: None.
    """
    try:
        # usa selenium para resolver
        driver = bot.driver
        origin = driver.find_element(By.ID, "column-a")
        destiny = driver.find_element(By.ID, "column-b")

        actions = ActionChains(driver=driver)

        # "fmt: off ignora formatação do black formatter"
        # fmt: off
        (
            actions.click_and_hold(origin)
            .move_to_element(destiny)
            .release()
            .perform()
        )
        logging.info("Movimentação de objeto html feita com sucesso.")
        return None
    except Exception as err:
        logging.error("Erro ao movimentar objeto html")
        format_error_message(err=err)
        sys.exit()
