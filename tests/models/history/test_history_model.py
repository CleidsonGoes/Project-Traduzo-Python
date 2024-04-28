import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    history_list = HistoryModel.list_as_json()
    data_list = json.loads(history_list)

    for data in data_list:
        assert "text_to_translate" in data
        assert "translate_from" in data
        assert "translate_to" in data
        assert not data["text_to_translate"].islower()

    assert data_list[1]["text_to_translate"] == "Do you love music?"
    assert data_list[1]["translate_from"] == "en"
    assert data_list[1]["translate_to"] == "pt"
