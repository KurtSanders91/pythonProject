from src import file_service
from mock import mock_open
import mock


def test_list_dir_succes_flow(mocker):
    list_dir_mock = mocker.patch("os.listdir")
    list_dir_mock.return_value = ["a"]

    res = file_service.list_dir()

    list_dir_mock.assert_called_once()
    assert res == ["a"]

def test_create_file_success(mocker):
    # AAA Arrange Act Assert

    mocked_open = mock_open()
    mocker.patch("builtins.open", mocked_open, create=True)
    mocker.patch("src.utils.random_string").return_value = "test_random_string"

    file_service.create_file("blabla")

    mocked_open.assert_called_with("test_random_string", "w")
    mocked_open().write.assert_called_with("blabla")


def test_create_file_dublicate(mocker):
    mocked_open = mock_open()
    mocker.patch("builtins.open", mocked_open, create=True)

    path_exist_mock = mocker.patch("os.path.exists")

    path_exist_call_count = 0
    def on_path_exist_call(filename):
        nonlocal path_exist_call_count
        path_exist_call_count += 1
        if path_exist_call_count == 2:
            assert filename == "another_random_string"
            return False
        assert filename == "test_random_string"
        return True

    path_exist_mock.side_effect = on_path_exist_call

    random_string_mock = mocker.patch("src.utils.random_string")

    def random_string_side_effect(length):
        if len(random_string_mock.mock_calls) == 1:
            return "test_random_string"
        return "another_random_string"
    random_string_mock.side_effect = random_string_side_effect

    file_service.create_file("blabla")

    assert path_exist_mock.mock_calls == [mock.call("test_random_string"),
                                          mock.call("another_random_string")]

    mocked_open.assert_called_with("another_random_string", "w")
    mocked_open().write.assert_called_with("blabla")