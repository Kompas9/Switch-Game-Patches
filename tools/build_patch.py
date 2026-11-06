"""Recreate the v1.0 IPS. Optional input is a decompressed NSO memory-layout dump."""
from pathlib import Path
import argparse
import hashlib
import struct

BUILD_ID = 'DB93B0125F4850601D61C3EDDE012F8EB2ECFE77'
INPUT_SHA256 = '0d3780b1cc70a48d46343dce05d26da535799faa096cf666e7841bc25fc6a20c'
PATCH_SHA256 = 'f233c0b3dc046db9ecab8c85e072b2d6fc86a431de8918effbefa236ca3a66e2'
SITES = [(0x5D18C, bytes.fromhex('F603042A'), bytes.fromhex('36008052')),
         (0x7BF1AC, bytes.fromhex('C9038052'), bytes.fromhex('89078052'))]

def make_patch():
    patch = bytearray(b'PATCH')
    for address, _, new in SITES:
        patch += (address+0x100).to_bytes(3,'big') + len(new).to_bytes(2,'big') + new
    patch += b'EOF'
    assert hashlib.sha256(patch).hexdigest() == PATCH_SHA256
    return bytes(patch)

def verify_dump(path):
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != INPUT_SHA256:
        raise ValueError('Not the exact supported decompressed memory-layout NSO dump.')
    assert data[:4] == b'NSO0'
    assert data[0x40:0x60].hex().upper() == BUILD_ID.ljust(64,'0')
    for address, old, _ in SITES:
        assert data[address+0x100:address+0x104] == old
    return data

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-dump',type=Path,help='Optional original decompressed NSO; never modified.')
    parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parents[1]/'60FPS-v1.0/exefs'/f'{BUILD_ID}.ips')
    args = parser.parse_args()
    if args.verify_dump:
        verify_dump(args.verify_dump)
        print('Supported input hash, build ID and original instructions verified.')
    patch = make_patch()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_bytes(patch)
    print(f'{args.output}: {len(patch)} bytes; SHA256 {PATCH_SHA256}')

if __name__ == '__main__':
    main()
