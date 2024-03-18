from pathlib import Path
import pytest
from pact import Consumer, Provider


@pytest.fixture(scope='module')
def pact_fixt(request):
    base_dir = Path(__file__).parent.parent
    data = request.getfixturevalue('prep_data')
    pact = Consumer(data['consumer']).has_pact_with(
        Provider(data['provider']), host_name=data['host_name'], port=data['port'],
        pact_dir=Path(base_dir, 'pacts').__str__(),
        log_dir=Path(base_dir, 'logs').__str__())
    try:
        print('start service')
        pact.start_service()
        yield pact
    finally:
        print('stop service')
        pact.stop_service()
