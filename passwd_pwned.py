#!/usr/bin/python3

import hashlib
import sys
import requests

passwd = sys.argv[1]
print(f"Checking password {sys.argv[1]}")
m = hashlib.sha1()
m.update(passwd.encode())
digest = m.hexdigest()

r = requests.get(f'https://api.pwnedpasswords.com/range/{digest[0:5]}')

if r.status_code != 200:
  print(f'HTTP request failed, with exit code {r.status_code}')
  sys.exit(1)

matching_passwd_list = r.text.splitlines()
for matching_passwd in matching_passwd_list:
  if digest.upper()[6:] in matching_passwd:
    print(f'{passwd} is compromised!')
    print(f"Hash: {matching_passwd.split(':')[0]}")
    print(f"Occurrences: {matching_passwd.split(':')[1]}")
    exit(0)

print(f'{passwd} not compromised!')
