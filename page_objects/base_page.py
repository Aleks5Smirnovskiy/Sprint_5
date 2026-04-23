from selenium.common.exceptions import ElementNotInteractableException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import Timeouts


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Timeouts.WAIT_TIMEOUT)

    def open(self, url):
        self.driver.get(url)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.wait_clickable(locator).click()

    def fill(self, locator, text):
        element = self.wait_present(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
            element.send_keys(Keys.CONTROL, "a")
            element.send_keys(Keys.DELETE)
            element.send_keys(text)
        except ElementNotInteractableException:
            self.driver.execute_script(
                """
                arguments[0].value = arguments[1];
                arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
                arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
                """,
                element,
                text,
            )

    def get_text(self, locator):
        return self.wait_visible(locator).text

    def get_attribute(self, locator, attribute_name):
        return self.wait_visible(locator).get_attribute(attribute_name)

    def get_computed_style(self, locator, style_name):
        element = self.wait_visible(locator)
        return self.driver.execute_script(
            "return window.getComputedStyle(arguments[0]).getPropertyValue(arguments[1]);",
            element,
            style_name,
        )

    def wait_url_contains(self, value):
        self.wait.until(EC.url_contains(value))

    def wait_url_changes(self, previous_url):
        self.wait.until(EC.url_changes(previous_url))

    def is_visible(self, locator):
        try:
            self.wait_visible(locator)
        except TimeoutException:
            return False
        return True

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def get_current_url(self):
        return self.driver.current_url
