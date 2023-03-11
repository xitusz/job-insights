from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    file = read_brazilian_file('tests/mocks/brazilians_jobs.csv')

    for item in file:
        assert "title" and "salary" and "type" in item
