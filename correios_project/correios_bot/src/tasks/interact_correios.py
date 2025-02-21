from botcity.web import WebBot, By


def interact_correios(
    bot: WebBot,
    service_type: str,
    cep_destiny: str,
    cep_origin: str = "38182428",
    shipping_date: str = None,
) -> None:
    """Coordena os subprocessos realizados no site dos correios.

    O parâmetro shipping_date é opcional. Valor padrão None.
    O valor é passado para a função _interact_data.

    O parâmetro cep_origin é opcional. Valor padrão "38182428".
    O valor é passado para a função _interact_cep.

    Args:
        bot (WebBot): instância da classe WebBot.
        shipping_date (str): data no formato ddmmaaaa. Valor padrão None.
        cep_origin (str): cep de origem para envio de encomenda.
        cep_destiny (str): cep de destino para envio de encomenda.
        service_type (str): string contendo tipo de serviço dos correios.
            Exemplo: 'PAC', 'SEDEX', 'SEDEX 10' etc.

    Return: None.
    """

    _interact_data(bot=bot, shipping_date=shipping_date)
    _interact_cep(bot=bot, cep_destiny=cep_destiny, cep_origin=cep_origin)
    _interact_object(bot=bot, service_type=service_type)

    _interact_response_correios()
    _fill_planilha()


# ok
def _interact_data(bot: WebBot, shipping_date: str) -> None:
    """Preenche data de postagem no site dos correios.

    Args:
        bot (WebBot): instância da classe WebBot.
        shipping_date (str): data no formato ddmmaaaa.

    Return: None.
    """

    try:
        if shipping_date:
            bot.find_element("input#data", By.CSS_SELECTOR).clear()
            bot.find_element("input#data", By.CSS_SELECTOR).click()
            bot.paste(shipping_date)
        # inserir logging com info "data de postagem alterada com sucesso."
        else:
            ...  # inserir logging com info "Data de postagem não alterada."
        return None
    except Exception as err:
        ...  # inserir função error
        raise


# ok
def _interact_cep(
    bot: WebBot,
    cep_origin: str,
    cep_destiny: str,
) -> None:
    """Preenche cep de origem e destino no site dos correios.

    Args:
        bot (WebBot): instância da classe WebBot.
        cep_origin (str): cep de origem para envio de encomenda.
        cep_destiny (str): cep de destino para envio de encomenda.

    Return: None.
    """

    bot.find_element("//input[@name='cepOrigem']", By.XPATH).click()
    bot.paste(cep_origin)
    bot.find_element("//input[@name='cepDestino']", By.XPATH).click()
    bot.paste(cep_destiny)
    return None


def _interact_object(bot: WebBot, service_type: str):
    """Coordena os subprocessos de serviços no site dos corrreios.

    Args:
        bot (WebBot): instância da classe WebBot.
        service_type (str): string contendo tipo de serviço dos correios.
            Exemplo: 'PAC', 'SEDEX', 'SEDEX 10' etc.

    """
    # interact type
    bot.find_element(
        "//select[@name='servico']",
        By.XPATH,
    ).send_keys(service_type)
    # interact format
    package_format = "caixa"  # virar parametro
    bot.find_element(f"img.{package_format}", By.CSS_SELECTOR).click()
    # interact_package
    package_type = "Outra Embalagem"  # virar parametro
    bot.find_element(
        "//select[@name='embalagem1']",
        By.XPATH,
    ).send_keys(package_type)
    # interact_dimensions
    altura = "30"
    largura = "22"
    comprimento = "13"
    bot.find_element("//input[@name='Altura']", By.XPATH).click()
    bot.paste(altura)
    bot.tab()
    bot.paste(largura)
    bot.tab()
    bot.paste(comprimento)
    # interact_weight
    weight = "5"  # virar parametro
    bot.find_element(
        "//select[@name='peso']",
        By.XPATH,
    ).send_keys(weight)
    # interact_button
    bot.find_element("input.btn2", By.CSS_SELECTOR).click()


def _interact_response_correios():
    """Capta informações no site dos correios."""
    ...


def _fill_planilha():
    """Preenche a planilha com as informações do site dos correios."""
    ...
