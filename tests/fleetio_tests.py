from fleetio import FleetIO
from nose.tools import *


class testFleetIO(object):
    def test_trivial_pass(self):
        assert_equal(1, 1)

    def test_init(self):
        f = FleetIO('', '')
        assert_equal(f.api_key, f.account_token, '')


    def test_invalid_api_keys(self):
        f = FleetIO('')
        r = f.api_get('vehicles', 'ID', 'meter_entries')
        assert_equal(r.status_code, 403)
