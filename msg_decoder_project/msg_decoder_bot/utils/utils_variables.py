from datetime import datetime
from pathlib import Path

# URLs
URL_SOURCE = (
    "https://pathfinder.automationanywhere.com/challenges/"
    "AutomationAnywhereLabs-Translate.html?_gl=1*uoc654*_g"
    "cl_au*Mjg2MDA3MjczLjE3Mzg5Mjc2MjA.*_ga*MTE4MDQzMTk1NC"
    "4xNzM4OTI3NjIw*_ga_DG1BTLENXK*MTczOTI3MjQ4My4zLjEuMTc"
    "zOTMwNDU0Ni41OC4wLjE4NTcwMDM5MzI."
)

URL_TRADUTOR = "https://translate.glosbe.com/bg-en"

# variáveis
LOGFILE_KEY_NAME = datetime.now().strftime("%Y%m%d%H%M")

ENV_PATH = Path(__file__).parent / ".env"

# SELECTORS
XPATH_ACCEPT_COOKIES = '//*[@id="onetrust-accept-btn-handler"]'
XPATH_COMMUNITY_BUTTON = (
    '//button[@id="button_modal-login-btn__iPh6x" and text()="Community login"]'
)
XPATH_NAME_LOGIN = '//input[@id="43:2;a"]'
XPATH_NEXT_BUTTON = '//button[text()="Next"]'
XPATH_LOGIN_BUTTON = '//button[text()="Log in"]'