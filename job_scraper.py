from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Set up ChromeDriver
service = Service("/usr/local/bin/chromedriver")  # Path to ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode (no UI)
driver = webdriver.Chrome(service=service, options=options)

# Job search URL (only Indeed for now)
job_urls = [
    "https://www.indeed.com/jobs?q=ER+Nurse&l=Las+Vegas%2C+NV"
]

# Scrape job listings
job_listings = []
for url in job_urls:
    driver.get(url)
    time.sleep(5)  # Wait for page to load

    jobs = driver.find_elements(By.CLASS_NAME, "job_seen_beacon")  # Modify this selector for each platform
    for job in jobs:
        try:
            title = job.find_element(By.TAG_NAME, "h2").text.strip()
            company = job.find_element(By.CLASS_NAME, "companyName").text.strip()
            salary = job.find_element(By.CLASS_NAME, "salary-snippet").text.strip() if job.find_elements(By.CLASS_NAME, "salary-snippet") else "Not Listed"
            link = job.find_element(By.TAG_NAME, "a").get_attribute("href")

            job_listings.append({"Title": title, "Company": company, "Salary": salary, "Link": link})
        except:
            continue

# Close the browser
driver.quit()

# Print results (for testing)
for job in job_listings:
    print(job)

