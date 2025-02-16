import logging
import traceback


def custom_error_message(err: Exception) -> None:
    """Defina o formato da exception que é enviada ao logfile."""

    lineno = traceback.extract_tb(err.__traceback__)[-1].lineno
    logging.error(f"{type(err).__name__}:{err} - Linha: {lineno}")
