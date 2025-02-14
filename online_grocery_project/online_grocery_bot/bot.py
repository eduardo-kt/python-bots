import os
from dotenv import load_dotenv
from botcity.maestro import BotMaestroSDK
from utils import utils_setup, utils_variables

load_dotenv()
username_aa = os.getenv('AA_CREDENTIAL_USERNAME')
password_aa = os.getenv('AA_CREDENTIAL_PASSWORD')

BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():

    # Inicia Log
    utils_setup.logfile_setup()

    # Configura Maestro
    maestro, execution = utils_setup.maestro_setup()

    # Instancia Bot
    webbot = utils_setup.web_bot_setup(
            URL=utils_variables.URL_SOURCE
    )

    # Login em Area Community
    utils_setup.login_community(bot=webbot,
                                username=username_aa,
                                password=password_aa)

    # Download e preparo de csv
    csv_data_as_list = utils_setup.csv_routine(bot=webbot)

    # Iterar dados na URL
    utils_setup.fill_url_with_data(
        data=csv_data_as_list,
        bot=webbot
    )

    # Finalizar processo na URL
    utils_setup.close_process(bot=webbot)

    # Maestro closure
    utils_setup.maestro_closure(wait_time=2000,
                                bot=webbot,
                                execution=execution,
                                maestro=maestro)


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
