from botcity.web import WebBot, By


def interact_correios(bot: WebBot):
    """Coordena os subprocessos realizados no site dos correios."""

    _interact_data(bot=bot, postagem="25022025")
    _interact_cep()
    _interact_object()

    _interact_response_correios()
    _fill_planilha()


def _interact_data(bot: WebBot, postagem: str = None) -> None:
    """Preenche data de postagem no site dos correios.

    Args:
        postagem (str): data no formato ddmmaaaa. Padrão é None.

    """
    try:
        if postagem:
            bot.find_element("input#data", By.CSS_SELECTOR).clear()
            bot.find_element("input#data", By.CSS_SELECTOR).click()
            bot.paste(postagem)
        # inserir logging com info "data de postagem alterada com sucesso."
        else:
            ...  # inserir logging com info "Data de postagem não alterada."
        return None
    except Exception as err:
        ...  # inserir função error

        raise


def _interact_cep():
    """Preenche cep de origem e destino no site dos correios."""
    ...


def _interact_object():
    """Coordena os subprocessos de serviços no site dos corrreios."""

    _interact_type()
    _interact_format()
    _interact_embalagem()
    _interact_dimensions()
    _interact_peso()
    _interact_button()


def _interact_type():
    """Define o tipo de serviço que será realizado no site dos correios."""
    ...


def _interact_format():
    """Define o formato da embalagem que será utilizada."""
    ...


def _interact_embalagem():
    """Define a classe de embalagem que será utilizada."""
    ...


def _interact_dimensions():
    """Preenche as dimensões da embalagem que será utilizada."""
    ...


def _interact_peso():
    """Preenche o peso estimado da embalagem que será utilizada."""
    ...


def _interact_button():
    """Clica no botão calcular do site dos correios."""
    ...


def _interact_response_correios():
    """Capta informações no site dos correios."""
    ...


def _fill_planilha():
    """Preenche a planilha com as informações do site dos correios."""
    ...
