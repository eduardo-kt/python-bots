from datetime import datetime

# variáveis
LOGFILE_KEY_NAME = datetime.now().strftime("%Y%m%d%H%M")

# URLs
URL_SOURCE = (
    "https://pathfinder.automationanywhere.com/challenges/Automatio"
    "nAnywhereLabs-ShoppingList.html?_gl=1*zvbndc*_gcl_au*Mjg2MDA3M"
    "jczLjE3Mzg5Mjc2MjA.*_ga*MTE4MDQzMTk1NC4xNzM4OTI3NjIw*_ga_DG1BT"
    "LENXK*MTczOTQzODQ0My41LjAuMTczOTQzODQ0Ni41Ny4wLjc5NDIxNTU2MQ.."
)

# Selectors para acesso área Community
XPATH_ACCEPT_COOKIES = '//*[@id="onetrust-accept-btn-handler"]'
XPATH_COMMUNITY_BUTTON = (
    '//button[@id="button_modal-login-btn'
    '__iPh6x" and text()="Community login"]'
)
XPATH_NAME_LOGIN = '//input[@id="43:2;a"]'
XPATH_NEXT_BUTTON = '//button[text()="Next"]'
XPATH_LOGIN_BUTTON = '//button[text()="Log in"]'
