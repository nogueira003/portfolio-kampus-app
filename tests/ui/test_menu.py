from selenium.webdriver.common.by import By

def test_navegacao(driver, url_local, time):
    driver.get(url_local)
    ids_links = ["home", "about", "course", "contact"]

    for link_id in ids_links:
        time.sleep(3)
        link = driver.find_element(By.ID, link_id)
        print(f"Clicando no link com id: {link_id}")
        link.click()

    time.sleep(3)
    