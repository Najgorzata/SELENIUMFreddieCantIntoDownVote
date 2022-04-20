#Import bibliotek
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

piosenka = 'Crazy little thing called love Queen'
# przegladarka = input("Wybierz przeglądarkę wpisz chrome lub firefox: ")
przegladarka = "chrome"


class TestingFreddie(unittest.TestCase):

    def setUp(self):

        #Wybór przeglądarki
        if przegladarka == "firefox":
            self.browser = webdriver.Firefox()
        elif przegladarka == "chrome":
            self.browser = webdriver.Chrome()
        else:
            print("Przeglądarka nieobsługiwana")

        #Uruchomienie YT
        self.browser.get("https://www.youtube.com/")
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        # Wyszukanie i zaakceptowanie cookies
        agree_button = self.browser.find_element(By.CSS_SELECTOR,'ytd-button-renderer.ytd-consent-bump-v2-lightbox:nth-child(2) > a:nth-child(1) > tp-yt-paper-button:nth-child(1) > yt-formatted-string:nth-child(1)')
        agree_button.click()
        # Wyszukanie utworu
        time.sleep(2)
        szukaj = self.browser.find_element(By.XPATH, '//input[@name="search_query"]')
        szukaj.send_keys(piosenka)
        time.sleep(2)
        self.browser.find_element(By.XPATH, '//button[@id="search-icon-legacy"]').click()
        self.browser.find_element(By.XPATH, '//a[@id="video-title"][1]').click()

    def testUpvote(self):
        time.sleep(2)
        #Znajdź i kliknij łapkę w górę
        upVote = self.browser.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div[1]/ytd-toggle-button-renderer[1]/a/yt-icon-button/button/yt-icon')
        upVote.click()
        # Jeśli wyświetla się monit o zalogowanie, pass
        if self.browser.find_element(By.XPATH, '//iframe[@name="passive_signin"]').is_displayed():
            pass

    def testDownvote(self):
        time.sleep(2)
        #Znajdź i kliknij łapkę w dół
        downVote = self.browser.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div[1]/ytd-toggle-button-renderer[2]/a/yt-icon-button/button/yt-icon')
        downVote.click()
        #Jeśli wyświetla się monit o zalogowanie, pass
        if self.browser.find_element(By.XPATH, '//iframe[@name="passive_signin"]').is_displayed():
            pass

    def testComment(self):
        time.sleep(2)
        self.browser.execute_script("window.scrollTo(0, 1000)")
        time.sleep(2)
        # Znajdź pole komentarza
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="placeholder-area"]'))).click()
        #Jeśli wyświetla się pole logowania, pass
        if self.browser.find_element(By.XPATH, '//input[@id="identifierId"]').is_displayed():
            pass

    def tearDown(self):
        self.browser.quit()



if __name__ == '__main__':
    unittest.main()
