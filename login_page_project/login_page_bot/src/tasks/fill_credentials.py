import os
import sys
import logging
from pathlib import Path
from dotenv import load_dotenv
from botcity.web import WebBot, By
from src.utils.customize_error import custom_error_message

load_dotenv(dotenv_path=os.path.join(Path.cwd(), "data", ".env"))
username = os.getenv("LOGIN_USERNAME")
password = os.getenv("LOGIN_PASSWORD")


def fill_credentials(bot: WebBot) -> None:
    """Preenche as credenciais na URL e executa login."""

    try:
        bot.find_element("input#username", By.CSS_SELECTOR).send_keys(username)
        bot.find_element("input#password", By.CSS_SELECTOR).send_keys(password)
        bot.find_element("i.fa", By.CSS_SELECTOR).click()
        logging.info("Sucesso ao preencher credenciais na URL.")
    except Exception as err:
        logging.error("Erro ao preencher credenciais na URL.")
        custom_error_message(err=err)
        sys.exit()
