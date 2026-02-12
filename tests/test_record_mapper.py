from infrastructure.mappers.record_mapper import RecordMapper

def test_to_object_maps_one_item(mocker):
    mapper = RecordMapper()
    mapper.mesure_factory = mocker.Mock()
    mapper.mesure_factory.get_mesure.side_effect = ["T", "H", "P"]

    data = {"results": [{
        "id": "1",
        "heure_de_paris": "2026-02-11T10:00:00+01:00",
        "temperature_en_degre_c": "25.5",
        "humidite": "60",
        "pression": "101325",
    }]}

    records = mapper.to_object(data)

    assert len(records) == 1
    r = records[0]
    assert r.id == 1
    assert r.paris_date == "2026-02-11T10:00:00+01:00"
    assert r.temperature == "T"
    assert r.humidity == "H"
    assert r.pressure == "P"

    mapper.mesure_factory.get_mesure.assert_any_call("temperature", 25.5)
    mapper.mesure_factory.get_mesure.assert_any_call("humidity", 60.0)
    mapper.mesure_factory.get_mesure.assert_any_call("pressure", 1013)  # 101325 // 100



def test_to_object_returns_empty_when_no_results():
    mapper = RecordMapper()
    assert mapper.to_object({}) == []


def test_to_object_skips_bad_item(mocker):
    mapper = RecordMapper()
    mapper.mesure_factory = mocker.Mock()
    mapper.mesure_factory.get_mesure.side_effect = ["T", "H", "P"]

    data = {"results": [
        {"id": "x"},  # int("x") => erreur
        {"id": "2", "heure_de_paris": "ok", "temperature_en_degre_c": "1", "humidite": "2", "pression": "100000"},
    ]}

    records = mapper.to_object(data)

    assert len(records) == 1
    assert records[0].id == 2