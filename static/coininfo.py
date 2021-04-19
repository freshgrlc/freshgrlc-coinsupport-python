
#
#   Hardcoded coin info, expand at will
#

GRLC = {
    'name':                 'Garlicoin',
    'ticker':               'GRLC',
    'bech32_prefix':        'grlc',
    'address_version':      38,
    'p2sh_address_version': 50,
    'privkey_version':      176,
    'segwit_info': {
        'addresstype':      'base58',
        'address_version':  73,
        'receive_only':     True
    },
    'coindaemon': {
        'port':             42068
    }
}


TGRLC = {
    'name':                 'Garlicoin Testnet',
    'ticker':               'tGRLC',
    'bech32_prefix':        None,
    'address_version':      111,
    'p2sh_address_version': 58,
    'privkey_version':      239,
    'segwit_info':          None,
    'coindaemon': {
        'port':             42070
    }
}


TUX = {
    'name':                 'Tuxcoin',
    'ticker':               'TUX',
    'bech32_prefix':        'tux',
    'address_version':      65,
    'p2sh_address_version': 64,
    'privkey_version':      193,
    'segwit_info': {
        'addresstype':      'bech32',
        'address_prefix':   'tux',
        'receive_only':     False
    },
    'coindaemon': {
        'port':             42072
    }
}
