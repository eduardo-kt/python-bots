from botcity.maestro import BotMaestroSDK
from src.utils.log_utils import setup_logging
from src.utils.variables import URL_CORREIOS
from src.tasks.setup_webbot import setup_webbot
from src.tasks.maestro_tasks import finalize_maestro, initialize_maestro
from src.tasks.interact_correios import interact_correios


BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():

    setup_logging()

    maestro, execution = initialize_maestro()

    bot = setup_webbot(URL=URL_CORREIOS)

    interact_correios(
        bot=bot,
        cep_destiny="95913212",
        shipping_date="25022025",
        service_type="SEDEX",
    )

    finalize_maestro(
        wait_time=3000,
        bot=bot,
        execution=execution,
        maestro=maestro,
    )


if __name__ == "__main__":
    main()
