

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

    def test_boolean_false_var(self):
        from configlib import getConfig
        res = getConfig('bar', False, self.config_path)
        assert res is False

    def test_boolean_true_var(self):
        from configlib import getConfig
        res = getConfig('bar', True, self.config_path)
        assert res is True
