from src.sorting import sort_by


MOCK = [
    {"min_salary": 2000, "max_salary": 4000},
    {"min_salary": 3000, "max_salary": 7000},
    {"min_salary": 1500, "max_salary": 3000},
]


sorted_min = [MOCK[2], MOCK[0], MOCK[1]]
sorted_max = [MOCK[1], MOCK[0], MOCK[2]]


def test_sort_by_criteria():
    sort_by(MOCK, "min_salary")
    assert MOCK == sorted_min

    sort_by(MOCK, "max_salary")
    assert MOCK == sorted_max