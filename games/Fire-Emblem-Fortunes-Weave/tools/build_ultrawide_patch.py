"""Recreate the 3440x1440 ultrawide IPS32; optionally verify an original NSO dump."""
from pathlib import Path
import argparse
import hashlib
import json

def main():
    root=Path(__file__).resolve().parents[1]
    info=json.loads((root/'ultrawide-patch-records.json').read_text(encoding='utf-8'))
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-dump',type=Path,help='Original decompressed memory-layout NSO; never modified.')
    parser.add_argument('--output',type=Path,default=root/'Ultrawide-3440x1440-v1.2/exefs'/(info['build_id']+'.ips'))
    args=parser.parse_args()
    if args.verify_dump:
        data=args.verify_dump.read_bytes()
        if hashlib.sha256(data).hexdigest()!=info['input_decompressed_nso_sha256']:
            raise ValueError('Not the exact supported decompressed NSO memory-layout dump.')
        if data[:4]!=b'NSO0' or data[64:96].hex().upper()!=info['build_id'].ljust(64,'0'):
            raise ValueError('NSO header or build ID mismatch.')
        for record in info['records']:
            offset=int(record['address'],0)+0x100
            original=bytes.fromhex(record['original'])
            if data[offset:offset+len(original)]!=original:
                raise ValueError(f'Original bytes mismatch at {offset:#x}.')
    patch=bytearray(b'IPS32')
    ranges=[]
    for record in info['records']:
        offset=int(record['address'],0)+0x100;replacement=bytes.fromhex(record['replacement'])
        if not 0<len(replacement)<=65535:raise ValueError('Invalid record length.')
        if any(not(offset+len(replacement)<=a or b<=offset) for a,b in ranges):
            raise ValueError('Overlapping patch records.')
        ranges.append((offset,offset+len(replacement)))
        patch+=offset.to_bytes(4,'big')+len(replacement).to_bytes(2,'big')+replacement
    patch+=b'EEOF'
    digest=hashlib.sha256(patch).hexdigest()
    if digest!=info['patch_sha256']:raise ValueError('Patch hash mismatch.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_bytes(patch)
    print(f'{args.output}: {len(info["records"])} records, {len(patch)} bytes; SHA256 {digest}')

if __name__=='__main__':main()
