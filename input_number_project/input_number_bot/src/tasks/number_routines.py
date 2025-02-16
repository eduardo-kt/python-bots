import sys
import logging
from pathlib import Path
from botcity.web import WebBot, By
from src.utils.customize_error import custom_error_message


def fill_and_save_value(bot: WebBot, number: int) -> None:
    """Executa subrotinas fill_number e save_value_to_file."""

    try:
        _fill_number(bot, number)
        _save_value_to_file(bot)
    except Exception as err:
        logging.error("Erro na execução de subrotina.")
        custom_error_message(err=err)
        sys.exit()


def _fill_number(bot: WebBot, number: int) -> None:
    """Insere número no campo da URL."""

    try:
        bot.find_element("input", By.CSS_SELECTOR).send_keys(number)
        logging.info("Sucesso ao preencher número em campo da URL.")
    except Exception as err:
        logging.error("Erro ao preencher número em campo da URL.")
        custom_error_message(err=err)
        raise


def _save_value_to_file(bot: WebBot) -> None:
    """Salva número digitado em arquivo .txt."""

    try:
        value = bot.find_element(
            "input",
            By.CSS_SELECTOR,
        ).get_attribute("value")
        data_dir = Path.cwd() / "data"
        data_dir.mkdir(parents=True, exist_ok=True)
        file_txt = data_dir / "values.txt"

        with file_txt.open("a", encoding="utf-8") as f:
            f.write(value + "/n")
        logging.info("Sucesso ao salvar campo da URL em arquivo value.txt.")
    except Exception as err:
        logging.error("Erro ao salvar campo da URL em arquivo value.txt.")
        custom_error_message(err=err)
        raise
