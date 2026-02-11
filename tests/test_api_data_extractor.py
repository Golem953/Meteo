import pytest
from infrastructure.extractor.api_data_extractor import APIDataExtractor


def test_extract_calls_api_client(mocker):
    # Arrange

    fake_file = "file.json"
    fake_response = {"data": f"{fake_file}"}

    # mock de l'instance
    mock_client_instance = mocker.Mock()
    mock_client_instance.call.return_value = fake_response

    # mock de la classe APIClient
    mock_client_class = mocker.patch(
        "infrastructure.extractor.api_data_extractor.APIClient",
        return_value=mock_client_instance
    )

    fake_config = object()

    # Act
    extractor = APIDataExtractor(fake_config)
    result = extractor.extract(fake_file, limit=123)

    # Assert
    mock_client_class.assert_called_once_with(fake_config)
    mock_client_instance.call.assert_called_once_with(123, fake_file)
    assert result == fake_response


def test_extract_uses_default_limit(mocker):
    fake_file = "file.json"
    fake_response = {"data": f"{fake_file}"}

    mock_client_instance = mocker.Mock()
    mock_client_instance.call.return_value = fake_response

    mocker.patch(
        "infrastructure.extractor.api_data_extractor.APIClient",
        return_value=mock_client_instance
    )

    extractor = APIDataExtractor(object())

    result = extractor.extract(fake_file)

    mock_client_instance.call.assert_called_once_with(200, fake_file)
    assert result == fake_response


def test_extract_propagates_exception(mocker):
    mock_client_instance = mocker.Mock()
    mock_client_instance.call.side_effect = RuntimeError("API down")

    mocker.patch(
        "infrastructure.extractor.api_data_extractor.APIClient",
        return_value=mock_client_instance
    )

    extractor = APIDataExtractor(object())

    with pytest.raises(RuntimeError, match="API down"):
        extractor.extract("data.json", limit=10)
