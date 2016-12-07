"""
--- Day 7: Internet Protocol Version 7 ---

While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.

For example:

abba[mnop]qrst supports TLS (abba outside square brackets).
abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
How many IPs in your puzzle input support TLS?

--- Part Two ---

You would also like to know which IPs support SSL (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.

For example:

aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).
How many IPs in your puzzle input support SSL?
"""
import re
ip_addresses = []

with open('day7.txt', 'r') as f:
  ip_addresses = f.readlines()

regex_abba = re.compile(r'(?!(\w)\1\1\1)(\w)(\w)\3\2') # ABBA, but not AAAA
regex_aba = re.compile(r'(?!(\w)\1\1)(\w)(\w)\2') # ABA, but not AAA
# regex_bab = re.compile('(?!(\w)\\1\\1)(\w)(\w)\\2') # ABBA, but not AAAA
regex_net = '\[\w+\]' # Between []

def count_tls(ip_addresses):
  tls_ips = 0
  for line in ip_addresses:
    if not line: continue
    line = line.strip()
    # ips between hypernet sequences []
    nets = (re.findall(regex_net, line))
    # ips outside of the net
    ips = (re.split(regex_net, line))
    if any([regex_abba.search(net) for net in nets]):
      continue
    if any([regex_abba.search(ip) for ip in ips]):
      tls_ips += 1

  return tls_ips

def supports_ssl(ips, nets):
  # Check all ABAs against BABs in the nets
  for aba in ips:
    regex_bab = re.compile('{}{}{}'.format(aba[1], aba[0], aba[1]))
    if any([regex_bab.search(net) for net in nets]):
      return True
  return False    

def count_ssl(ip_addresses):
  ssl_ips = 0
  for line in ip_addresses:
    if not line: continue
    line = line.strip()
    # ips between hypernet sequences []
    nets = (re.findall(regex_net, line))
    # ips outside of the net
    ips = (re.split(regex_net, line))
    for ip in ips:
      # Generate all ABA patterns in IP
      matches = [ip[i:i+3] for i in range(0, len(ip) - 2)
                if regex_aba.match(ip[i:i+3])]
      if matches and supports_ssl(matches, nets):
        ssl_ips += 1
        break

  return ssl_ips

# Part 1: IPs that support TLS
print (count_tls(ip_addresses))
# Part 2: IPs that support SSL
# ip_addresses = ['aba[bab]xyz', 'xyx[xyx]xyx', 'aaa[kek]eke', 'zazbz[bzb]cdb']
print (count_ssl(ip_addresses))

