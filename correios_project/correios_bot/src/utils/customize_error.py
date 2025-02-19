import logging
import traceback


def format_error_message(err: Exception) -> None:
    """
    Formata a exception que é enviada ao logfile.

    Args:
        err (Exception): objeto da classe Exception.

    Return: None.
    """

    lineno = traceback.extract_tb(err.__traceback__)[-1].lineno
    logging.error(f"{type(err).__name__}: {err} - Linha: {lineno}")
    return None
