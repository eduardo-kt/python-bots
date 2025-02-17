import os
import sys
import logging
from src.utils.variables import LOGFILE_KEY_NAME


def setup_logging() -> None:
    """
    Coordena a configuração do diretório de logs e a formatação dos logs.

    Args: None

    Return: None
    """

    try:
        logfile = _setup_log_directory()
        _configure_logging(logfile=logfile)
        logging.info("Sucesso ao iniciar arquivo de logs.")
    except Exception as err:
        print("Erro ao iniciar arquivo de logs.")
        print(f"{type(err).__name__}: {err}")
        sys.exit()


def _setup_log_directory(log_dir: str = "logs") -> str:
    """
    Configura o diretório de logs e retorna o caminho do arquivo de log.

    Args:
        log_dir (str): Nome do diretório que armazenará os logs.
            Valor padrão: "logs".

    Return:
        str: O caminho completo do arquivo de logs.
    """

    try:
        os.environ["WDM_LOG"] = str(logging.NOTSET)
        os.makedirs(log_dir, exist_ok=True)
        return os.path.join(log_dir, f"{LOGFILE_KEY_NAME}_logfile.log")
    except Exception as err:
        print("Erro ao configurar o diretório de logs.")
        print(f"{type(err).__name__}: {err}")
        raise


def _configure_logging(logfile: str) -> None:
    """
    Configura o sistema de logs e define o formato da saída dos logs.

    Args:
        logfile (str): o caminho completo do arquivo de logs.

    Return: None.
    """

    try:
        logging.basicConfig(
            level=logging.INFO,
            filename=logfile,
            filemode="w",
            format="%(asctime)s %(levelname)s, linha %(lineno)s, %(message)s",
            encoding="utf-8",
        )
        logging.info("Início do processo.")
        logging.info("Sucesso ao iniciar logfile na pasta logs.")
    except Exception as err:
        print("Erro durante inicialização do logging.")
        print(f"{type(err).__name__}: {err}")
        raise
