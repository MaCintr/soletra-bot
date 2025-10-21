from scraper.browser import iniciar_browser

def main():
    driver = iniciar_browser()
    driver.get("https://soletra.globo.com")



if __name__ == "__main__":
    main()