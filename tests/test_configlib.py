

class TestConfigLib(object):
    def setup(self):
        self.config_path = 'tests/fixture/fqdnblocklist.conf'

    def test_current_behavior(self):
        from configlib.configlib import getConfig

        res = getConfig('mongohost', 'defaultvalue', self.config_path)
        assert res == 'mongodb'
