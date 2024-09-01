import os

def build():
  os.system("sudo apt update")
  os.system("sudo apt install chromium-chromedriver chromium-browser")
  os.system("pip3 install selenium")
  os.system("pip3 install streamlit")
  os.system("pip3 install webdriver-manager")
  return None

build()
