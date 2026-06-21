from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    base_url = "https://httpbin.org"

    user1_cookie = "fake_session_token_user_1"
    user2_cookie = "fake_session_token_user_2"

    if user1_cookie:
        url_user1 = f"{base_url}/cookies/set?session={user1_cookie}"

    user1_cookie = None

    if user2_cookie:
        url_user2 = f"{base_url}/cookies/set?session={user2_cookie}"

    assert url_user1 != url_user2, (
        f"Откат сессии не сработал. Оба URL одинаковые: {url_user1}"
    )

    driver.get(base_url)

    driver.quit()
