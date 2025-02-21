from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Configure Chrome Options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")  # Required for Colab
options.add_argument("--disable-dev-shm-usage")  # Prevent resource issues
options.add_argument("--disable-gpu")  # Fix crashes
options.add_argument("--remote-debugging-port=9222")  # Prevent DevTools error
options.binary_location = "/usr/bin/google-chrome-stable"  # Use correct Chrome binary

# Set ChromeDriver path
service = Service("/usr/bin/chromedriver")

# Launch WebDriver
driver = webdriver.Chrome(service=service, options=options)
print("Chrome WebDriver launched successfully!")
driver.quit()
