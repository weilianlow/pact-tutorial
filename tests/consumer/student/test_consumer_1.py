import pytest
from pact import Like
import requests


@pytest.fixture(scope='module', autouse=True)
def prep_data(request):
    data = dict()
    data['consumer'] = 'student-consumer-1'
    data['provider'] = 'student-provider'
    data['host_name'] = 'localhost'
    data['path'] = '/get-student'
    data['port'] = 5000
    data['uri'] = f'http://localhost:5000/get-student'
    return data


@pytest.mark.parametrize('student,expected', [
    ('Amy', {'status': 0, 'body': {'name': 'Amy', 'age': 49,
                                   "education": ['Nanyang Technological University', 'Singapore Polytechnic']}}),
    ('Peter', {'status': 1, "error": "Peter is not available"}),
])
def test_get_student(student, expected, request):
    query = {'name': student}
    data = request.getfixturevalue('prep_data')
    pact_fixt = request.getfixturevalue('pact_fixt')
    (pact_fixt
     .given(f'a student by the name of {student}')
     .upon_receiving('a request to get a student')
     .with_request(method='GET', path=data['path'], query=query)
     .will_respond_with(200, body=Like(expected)))

    with pact_fixt:
        response = requests.get(data['uri'] + '?' + '&'.join({f'{k}={v}' for k, v in query.items()}))
        assert response.status_code == 200
        pact_fixt.verify()
