from selenium.webdriver.common.by import By

def test_envia_formulario_contact(driver, url_local, time):
    try:
        driver.get(url_local)
        time.sleep(3)  # espera a página carregar
        # Clica no menu contato
        contato = driver.find_element(By.ID, "contact")
        contato.click()
        time.sleep(3)  # espera carregar a página contato

        # Preenche o formulário
        driver.find_element(By.ID, "nome").send_keys("Robson Santos")
        driver.find_element(By.ID, "email").send_keys("robson@example.com")
        driver.find_element(By.ID, "mensagem").send_keys("Mensagem de teste via Selenium.")

        # Envia o formulário
        driver.find_element(By.ID, "mensagem").submit()

        time.sleep(1)  # espera página recarregar e mensagem aparecer

        # Verifica a mensagem de sucesso
        msg = driver.find_element(By.ID, "msg-sucesso").text
        assert "sucesso" in msg.lower(), f"Mensagem de sucesso não encontrada, texto atual: '{msg}'"
        print("######/n/n/n/nFormulário enviado e mensagem de sucesso confirmada!/n/n/n/n######")
    finally:
        driver.quit()
