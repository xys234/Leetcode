
import logging


class DispatchingFormatter:

    def __init__(self, formatters, default_formatter):
        self._formatters = formatters
        self._default_formatter = default_formatter

    def format(self, record):
        formatter = self._formatters.get(record.name, self._default_formatter)
        return formatter.format(record)


handler = logging.StreamHandler()
handler.setFormatter(DispatchingFormatter(
    {
        'base.foo': logging.Formatter('FOO: %(message)s'),
        'base.bar': logging.Formatter('BAR: %(message)s'),
    },
    logging.Formatter('%(message)s'),
)
)
logging.getLogger().addHandler(handler)

logging.getLogger('base.foo').error('Log from foo')
logging.getLogger('base.bar').error('Log from bar')
logging.getLogger('base.baz').error('Log from baz')


