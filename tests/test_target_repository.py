
from repositories.target_repository import find_all_targets, find_target_by_id
from services.target_sevice import convert_target_to_json


def test_find_all_targets():
    targets = find_all_targets()
    assert True


def test_find_target_by_id():
    target = find_target_by_id(1).unwrap()
    dict = convert_target_to_json(target)
    assert False
