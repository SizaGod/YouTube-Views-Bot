import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
def load_proxies(file_path):
    with open(file_path, 'r') as file:
        proxies = file.readlines()
    return [proxy.strip() for proxy in proxies]
def get_random_proxy(proxies):
    return random.choice(proxies)
def watch_video_with_proxy(proxy, video_url):
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument(f'--proxy-server={proxy}')
    
    driver = uc.Chrome(options=chrome_options)
    driver.get(video_url)
    try:
        play_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="ytp-large-play-button ytp-button"]'))
        )
        play_button.click()
        video_duration = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[@class="ytp-time-duration"]'))
        )
        duration = video_duration.text.split(':')
        if len(duration) == 2:
            total_seconds = int(duration[0]) * 60 + int(duration[1])
        else:
            total_seconds = int(duration[0]) * 3600 + int(duration[1]) * 60 + int(duration[2])
        time.sleep(total_seconds + 5)

    except Exception as e:
        print(f"Error : {e}")

    finally:
        driver.quit()
proxies_file_path = 'proxies.txt'
proxies = load_proxies(proxies_file_path)
video_url = 'https://www.youtube.com/watch?v=VIDEO_ID'
while True:
    proxy = get_random_proxy(proxies)
    watch_video_with_proxy(proxy, video_url)
