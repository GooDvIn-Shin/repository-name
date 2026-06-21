import pytest
import requests

# =====================================================================
# НАСТРОЙКИ ДЛЯ НАСТАВНИКА
# =====================================================================
BASE_URL = "https://yougile.com"  # Базовый URL API Yougile
TOKEN = "PLACE_YOUR_TOKEN_HERE"      # Авторизационный токен (Ключ API)


# =====================================================================
# ПАТТЕРН API CLIENT (PAGE OBJECT ДЛЯ API)
# =====================================================================
class ProjectsApiClient:

    def __init__(self, base_url: str, token: str):
        self.url = f"{base_url.rstrip('/')}/api-v2/projects"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

    def create_project(self, payload: dict) -> requests.Response:
        """[POST] /api-v2/projects"""
        return requests.post(self.url, json=payload, headers=self.headers)

    def get_project(self, project_id: str) -> requests.Response:
        """[GET] /api-v2/projects/{id}"""
        return requests.get(f"{self.url}/{project_id}", headers=self.headers)

    def update_project(
        self, project_id: str, payload: dict
    ) -> requests.Response:
        """[PUT] /api-v2/projects/{id}"""
        return requests.put(
            f"{self.url}/{project_id}",
            json=payload,
            headers=self.headers
        )


# =====================================================================
# FIXTURES (ФИКСТУРЫ PYTEST)
# =====================================================================
@pytest.fixture
def api_client():
    """Инициализирует клиент для работы с API проектов Yougile."""
    return ProjectsApiClient(BASE_URL, TOKEN)


@pytest.fixture
def created_project_id(api_client):
    """Автоматически создает проект и отдает его ID для тестов."""
    payload = {"title": "Фикстурный проект Yougile"}
    response = api_client.create_project(payload)

    if response.status_code != 201:
        pytest.fail(f"Не удалось подготовить тест-данные: {response.text}")

    return response.json().get("id")


# =====================================================================
# ТЕСТЫ ДЛЯ МЕТОДА: [POST] /api-v2/projects
# =====================================================================
def test_create_project_positive(api_client):
    """Позитивный: Создание проекта с валидным обязательным полем title."""
    payload = {"title": "Новый проект через API"}
    response = api_client.create_project(payload)

    assert response.status_code == 201
    body = response.json()
    assert "id" in body


def test_create_project_missing_title_negative(api_client):
    """Негативный: Создание проекта без обязательного поля title."""
    payload = {"users": {}}  # Отправляем данные без названия проекта
    response = api_client.create_project(payload)

    assert response.status_code == 400


# =====================================================================
# ТЕСТЫ ДЛЯ МЕТОДА: [GET] /api-v2/projects/{id}
# =====================================================================
def test_get_project_positive(api_client, created_project_id):
    """Позитивный: Получение существующего проекта Yougile по ID."""
    response = api_client.get_project(created_project_id)

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == created_project_id


def test_get_project_not_found_negative(api_client):
    """Негативный: Запрос проекта по несуществующему ID."""
    non_existent_id = "99999999-9999-9999-9999-999999999999"
    response = api_client.get_project(non_existent_id)

    assert response.status_code == 404


# =====================================================================
# ТЕСТЫ ДЛЯ МЕТОДА: [PUT] /api-v2/projects/{id}
# =====================================================================
def test_update_project_positive(api_client, created_project_id):
    """Позитивный: Изменение названия проекта Yougile."""
    payload = {"title": "Обновленное название проекта"}
    response = api_client.update_project(created_project_id, payload)

    assert response.status_code == 200


def test_update_project_invalid_id_negative(api_client):
    """Негативный: Попытка изменения проекта по невалидному ID."""
    payload = {"title": "Попытка изменения"}
    response = api_client.update_project("invalid-id-format", payload)

    assert response.status_code in [400, 404]
