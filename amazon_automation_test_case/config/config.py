from ssl import Options

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Amazon Türkiye URL
BASE_URL = "https://www.amazon.com.tr/"

# The brand to be searched in the search box
SEARCH_BRAND = "Samsung"

# Browser selection
BROWSER = "chrome"

CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument("--disable-notifications")
CHROME_OPTIONS.add_argument("--disable-notifications")
CHROME_OPTIONS.add_argument("--ignore-certificate-errors")
CHROME_DRIVER_SERVICE = Service(ChromeDriverManager().install())

# Maximum wait time for page load (seconds)
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 10
