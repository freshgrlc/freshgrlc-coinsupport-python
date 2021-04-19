from addresscodecs import decode_base58_address, encode_base58_address, decode_bech32_address, encode_bech32_address


class SegwitConverter(object):
    def __init__(self, addresstype, receive_only):
        self.addresstype = addresstype
        self.receive_only = receive_only
        self.parent = None

    def make_p2wpkh(self, address, receive):
        if not receive and self.receive_only:
            return None

        if len(address) == 20:
            pubkeyhash = address
        else:
            _, pubkeyhash = decode_base58_address(address, verify_version=(self.parent.address_version if self.parent is not None else None))

        return self.encode_segwit_address(pubkeyhash)

    def encode_segwit_address(self, pubkeyhash):
        raise NotImplementedError('%s.encode_segwit_address()' % self.__class__.__name__)

    def decode_address(self, address):
        raise NotImplementedError('%s.decode_address()' % self.__class__.__name__)


class VersionByteSegwitConverter(SegwitConverter):
    def __init__(self, addresstype, address_version, receive_only=True):
        super(VersionByteSegwitConverter, self).__init__(addresstype, receive_only)
        self.versionbyte = address_version

    def encode_segwit_address(self, pubkeyhash):
        return encode_base58_address(self.versionbyte, pubkeyhash)

    def decode_address(self, address):
        return decode_base58_address(address, verify_version=self.versionbyte)


class Bech32SegwitConverter(SegwitConverter):
    def __init__(self, addresstype, address_prefix, receive_only=False):
        super(Bech32SegwitConverter, self).__init__(addresstype, receive_only)
        self.prefix = address_prefix

    def encode_segwit_address(self, pubkeyhash):
        return encode_bech32_address(self.prefix, pubkeyhash)

    def decode_address(self, address):
        return decode_bech32_address(address, verify_prefix=self.prefix)


def get_converter_factory_for_address_type(address_type):
    try:
        return {
            'base58': VersionByteSegwitConverter,
            'bech32': Bech32SegwitConverter
        }[address_type]
    except KeyError:
        raise Exception('Invalid address type: ' + address_type)
