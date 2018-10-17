

class TestConfigLib(object):
    def setup(self):
        self.config_path = 'tests/fixture/fqdnblocklist.conf'

    def test_current_behavior(self):
        from configlib import getConfig

        res = getConfig('mongohost', 'defaultvalue', self.config_path)
        assert res == 'mongodb'

    def test_option_parser(self):
        from configlib import OptionParser

        o = OptionParser
        assert o is not None
