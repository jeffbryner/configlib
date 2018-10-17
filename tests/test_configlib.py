

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

    def test_list_returns_as_string(self):
        from configlib import getConfig
        res = getConfig('foo', 'zab,za', self.config_path)
        assert res == 'foo,bar'
        assert isinstance(res, str)
