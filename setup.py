import os

def pre_download_deps():
  os.system("sudo apt update")
  os.system("sudo apt install chromium-chromedriver chromium-browser")
  os.system("pip3 install selenium")
  os.system("pip3 install streamlit")
  return None
