import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Adam is a student that wants to write a CV for future use,
# he's heard there is a website where you can write your CV online

# He goes to the homepage
# browser = webdriver.Chrome(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'cromedriver.exe'))
browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'Home' in browser.title

# He sees the form he needs to complete in order to end up with a CV
# He enters his name first

# He has no work experience yet so he decides to skip that part

# Then he enters information about his education

# After that he enters some of his skills

# After he reads everything he has just written he decides to submit his CV,
# but he gets a prompt that says he hasn't entered his email and address and
# that he must enter them before submitting the CV

# He enters them and is then able to submit his CV
# He decides to go an check if his CV was indeed saved on the website
# He accesses the website again and sees that his CV was saved and can modify it again
