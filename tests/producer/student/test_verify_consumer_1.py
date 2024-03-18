from pathlib import Path

import pytest
from pact import Verifier


@pytest.fixture(scope='module')
def verifier():
    return Verifier(provider='StudentService', provider_base_url='http://localhost:5000')


@pytest.fixture(scope='module')
def base_dir():
    return Path(__file__).parent.parent.parent


def test_verify_consumer_1(verifier, base_dir):
    success, logs = verifier.verify_pacts(Path(base_dir, 'pacts', 'student-consumer-1-student-provider.json').__str__())
    assert success == 0
