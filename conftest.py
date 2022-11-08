import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options




language_list = ['ar', 'ca', 'cs', 'da', 'de', 'en-bg', 'el', 'es', 'fi', 'fr', 'it', 'ko', 'nl', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk', 'zh-hans']


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help='Choose language on CMD')

@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    # browser = None
    if language in language_list:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(20)
    else:
        raise pytest.UsageError(f'--language must be from {language_list}')
    yield browser
    print("\nquit browser..")
    browser.quit()