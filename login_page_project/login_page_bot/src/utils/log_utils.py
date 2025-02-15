import os
import sys
import logging
from src.utils.variables import LOGFILE_KEY_NAME


def loggin_startup() -> None:
    """
    Realiza os subprocessos setup_log_directory e configure_logging.

    """
    try:
        logfile = setup_log_directory()
        configure_logging(logfile=logfile)
        logging.info("Sucesso ao iniciar arquivo de logs.")
    except Exception as err:
        print("Erro ao iniciar arquivo de logs.")
        print(f"{type(err).__name__}: {err}")
        sys.exit()


def setup_log_directory(log_dir: str = "logs") -> str:
    """Configura o diretório de logs e retorna o caminho do arquivo de log."""
    try:
        os.environ["WDM_LOG"] = str(logging.NOTSET)
        os.makedirs(log_dir, exist_ok=True)
        return os.path.join(log_dir, f"{LOGFILE_KEY_NAME}_logfile.log")
    except Exception as err:
        print("Erro ao configurar o diretório de logs.")
        print(f"{type(err).__name__}: {err}")
        raise


def configure_logging(logfile: str) -> None:
    """Configura o sistema de logs e define o formato da saída."""
    try:
        logging.basicConfig(
            level=logging.INFO,
            filename=logfile,
            filemode="w",
            format="%(asctime)s %(levelname)s, linha %(lineno)d, %(message)s",
            encoding="utf-8",
        )
        logging.info("Início do processo.")
        logging.info("Sucesso ao iniciar logfile na pasta archive.")
    except Exception as err:
        print("Erro durante a inicialização do logging.")
        print(f"{type(err).__name__}: {err}")
        raise
