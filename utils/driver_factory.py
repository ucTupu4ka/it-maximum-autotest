from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class DriverFactory:
    @staticmethod
    def create_driver(
        browser: str,
        headless: bool,
    ):
        browser = browser.lower()

        if browser == "chrome":
            options = ChromeOptions()

            if headless:
                options.add_argument("--headless=new")

            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--no-sandbox")

            driver = webdriver.Chrome(options=options)

        elif browser == "firefox":
            options = FirefoxOptions()

            if headless:
                options.add_argument("--headless")

            driver = webdriver.Firefox(options=options)

            driver.maximize_window()

        else:
            raise ValueError(
                f"Unsupported browser: {browser}. "
                f"Supported browsers: chrome, firefox"
            )

        return driver
