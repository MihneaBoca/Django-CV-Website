import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# browser = webdriver.Chrome(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'cromedriver.exe'))
browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'Home' in browser.title
