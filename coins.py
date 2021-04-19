from coinsupport.static.coininfo import *


_COINS = None


def all():
    global _COINS
    if _COINS is None:
        import static.coininfo
        exports = filter(lambda k: k[0] != '_', static.coininfo.__dict__.keys())
        _COINS = [ static.coininfo.__dict__[k] for k in exports ]
    return _COINS


def get_by_filter(value, filter_func):
    filtered = list(filter(filter_func, all()))
    return filtered[0] if len(filtered) > 0 else None


def by_name(name):
    return get_by_filter(name, lambda coin: coin['name'].lower() == name.lower())


def by_ticker(ticker):
    return get_by_filter(ticker, lambda coin: coin['ticker'].lower() == ticker.lower())


def by_address_versions(p2pkh_address_version, p2sh_address_version):
    return get_by_filter(
        '{ p2pkh address version: %d, p2sh address version: %d }' % (p2pkh_address_version, p2sh_address_version),
        lambda coin: coin['address_version'] == p2pkh_address_version and coin['p2sh_address_version'] == p2sh_address_version
    )
