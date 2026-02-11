import pytest
from infrastructure.http.api_client import APIClient
from domain.config.configuration import Configuration

class FakeConfig:
    API_BASE_URL = "https://api.test.com/"
    API_RECORDS_URL = "unused"
    API_TIMEOUT = 5
    API_OPTIONS_URL = "options=true"


def test_call_returns_json(mocker):
    # 1) on crée une fausse réponse HTTP
    response = mocker.Mock()
    response.raise_for_status.return_value = None
    response.json.return_value = {"ok": True}

    # 2) on crée une fausse session requests
    session = mocker.Mock()
    session.get.return_value = response

    # 3) on patch requests.Session pour qu'APIClient utilise NOTRE session
    mocker.patch("infrastructure.http.api_client.requests.Session", return_value=session)

    client = APIClient(FakeConfig)

    data = client.call(limit=10, file_name="weather")

    session.get.assert_called_once_with(
        "https://api.test.com/weather/options=true&limit=10",
        timeout=5,
    )
    assert data == {"ok": True}


# integration
def test_call_real_api():
    config = Configuration()  # config réelle
    client = APIClient(config)

    data = client.call(limit=1, file_name="42-station-meteo-toulouse-parc-compans-cafarelli")
    assert isinstance(data, dict)
