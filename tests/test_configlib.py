

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
        print(res)
        assert res == 'foo,bar'
        assert isinstance(res, str)

    def test_failing_syslog_var(self):
        from configlib import getConfig
        res = getConfig('syslogport', 514, self.config_path)
        assert res == 514
