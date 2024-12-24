from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from faker import Faker
import random


Name = "(//*[@role='listitem']/descendant::input)[1]"
Age = "//*[@role='listitem'][2]/descendant::input"
CollegeName = "//*[@role='listitem'][4]/descendant::input"
Gender = "(//*[contains(text(),'?')])[1]"
WorkExperience = "//*[@role='listitem'][5]/descendant::div[@data-value='?']"
DevelopmentWorkshop = "//*[@role='listitem'][6]/descendant::div[@data-value='?']"
Semister = "//*[@role='listitem'][7]/descendant::div[@data-value='?']"
WorkshopAttended = "//*[@role='listitem'][8]/descendant::div[@data-answer-value='?']"
SkillsImproved = "//*[@role='listitem'][9]/descendant::div[@data-answer-value='?']"
Benificial = "(//*[contains(text(),'?')])[1]"
PreferTolearn = "//*[@role='listitem'][11]/descendant::div[@data-answer-value='?']"
Barriers = "//*[@role='listitem'][12]/descendant::div[@data-answer-value='?']"
PrimaryMotivation = "//*[@role='listitem'][13]/descendant::div[@data-answer-value='?']"
PlacementProspects = "//*[@role='listitem'][14]/descendant::div[@data-value='?']"
Submit = "//*[contains(text(),'Submit')]"

def get_fake_indian_name():
    fake = Faker('en_IN')
    return fake.name()

def get_random_age(min_age=22, max_age=30):
    return random.randint(min_age, max_age)

def get_random_gender():
    return random.choice(['Male', 'Female'])

def get_random_college():
    return random.choices(
        ['SIIB', 'BALAJI', 'PUMBA', 'NIBM'],
        weights=[80, 7, 7, 6],
        k=1
    )[0]

def get_random_number(max_value):
    return random.randint(1, max_value)

def get_random_yes_no_choice():
    return random.choice(['Yes', 'No'])

def get_random_semister():
    return random.choice(['1–2 times a semester', '3–5 times a semester','More than 5 times a semester'])

def get_random_workshop_attended():
    return random.choice(['Resume Writing', 'Interview Skills','Industry-Specific Career Guidance','Technical Skills relevant to your specialisation'])

def get_random_skills_improved():
    return random.choice(['Industry Knowledge', 'Resume Crafting','Corporate Etiquettes','Personal Branding'])

def get_random_benificial():
    return random.choice(['Practical Activities (e.g., mock interviews, case studies)', 'Theoretical Insights and Guidance','Networking Opportunities','Real-World Examples and Case Studies'])

def get_random_prerfer_to_learn():
    return random.choice(['Interactive role-playing', 'Lecture-style presentations','Online webinars','Case study analysis','Expert panel discussions'])

def get_random_barriers():
    return random.choice(['Lack of relevance to my career goals', 'Limited workshop availability','Insufficient depth of content','Delivery method not engaging'])
                         
def get_random_primary_motivation():
    return random.choice(['Skill Enhancement (e.g., technical, communication)', 'To prepare for placements','To build confidence and personal growth'])

def get_random_placement_prospects():
    return random.choice(['Yes, significantly', 'Yes, to some extent','No (Mention the reason below)'])

def enter_text(driver, xpath, text):
    try:
        # Wait until the element is present and visible
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        element.clear()
        element.send_keys(text)
    except Exception as e:
        print(f"Failed to enter text: {text} in xpath: {xpath}")
        print(e)
        # Use JavaScript to enter text
        script = f"document.evaluate('{xpath}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.value = '{text}';"
        driver.execute_script(script)

def click_element(driver, xpath):
    try:
        for _ in range(1):
            print(xpath)
            # Wait until the element is present and clickable
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.click()
    except Exception as e:
        print(f"Failed to click element at xpath: {xpath}")
        print(e)

def launch_browser(browser_name):
    if browser_name == 'chrome':
        chrome_options = ChromeOptions()
        # chrome_options.add_argument("--headless")  # Run headless if needed
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    elif browser_name == 'firefox':
        firefox_options = FirefoxOptions()
        # firefox_options.add_argument("--headless")  # Run headless if needed
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get("https://forms.gle/SqDzEZfSc2DfxbYg7")
    print(f"{browser_name} title: {driver.title}")
    enter_text(driver, Name, get_fake_indian_name())
    enter_text(driver, Age, str(get_random_age()))
    click_element(driver,Gender.replace('?',get_random_gender()))
    enter_text(driver,CollegeName , get_random_college())
    click_element(driver,WorkExperience.replace('?',get_random_yes_no_choice()))
    click_element(driver,DevelopmentWorkshop.replace('?',get_random_yes_no_choice()))
    click_element(driver,DevelopmentWorkshop.replace('?',get_random_yes_no_choice()))
    click_element(driver,Semister.replace('?',get_random_semister()))
    click_element(driver,Benificial.replace('?',get_random_benificial()))
    for i in range(get_random_number(4)):
     click_element(driver,WorkshopAttended.replace('?',get_random_workshop_attended()))

    for i in range(get_random_number(4)):
     click_element(driver,SkillsImproved.replace('?',get_random_skills_improved()))

    click_element(driver,Benificial.replace('?',get_random_benificial()))

    for i in range(get_random_number(5)):
     click_element(driver,PreferTolearn.replace('?',get_random_prerfer_to_learn()))

    for i in range(get_random_number(4)):
        click_element(driver,Barriers.replace('?',get_random_barriers()))

    for i in range(get_random_number(3)):
        click_element(driver,PrimaryMotivation.replace('?',get_random_primary_motivation()))

    for i in range(get_random_number(3)):
        click_element(driver,PlacementProspects.replace('?',get_random_placement_prospects()))

    click_element(driver,Submit);
    print("Closed browser")
    time.sleep(10)  # Keep the browser open for a while
    driver.quit()

if __name__ == "__main__":
    for i in range(10):
        browsers = ['chrome','chrome','chrome','chrome','chrome']
        with ThreadPoolExecutor(max_workers=len(browsers)) as executor:
            executor.map(launch_browser, browsers)
        print(i)
