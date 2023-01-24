# Write code in python to validate given IP addresses

## Constraints:
- No external libraries
- Not to use regex

## Tasks:
- Differentiate if the given IP address is IPv4 or IPv5
- If IPv4, check if the IP address meets all the requirements to be a valid IPv4 address
- If IPv6, check if the IP address meets all the requirements to be a valid IPv6 address. 

## Steps taken:
- Reviewing the requirements for valid IPv4 and IPv6 addresses: https://www.ibm.com/docs/en/ts3500-tape-library?topic=functionality-ipv4-ipv6-address-formats

### IPv4
- Format:  x . x . x . x
- each octet separated by "."
- the number of "." must be 3.
- values must be between 0 - 255

### IPv6
- Format: y : y : y : y : y : y : y : y
- each segment separated by ":"
- the number of ":" must be between 2 and 7
- each segment can be any hexadecimal value between 0 and FFFF
- segments with only 0s can be represented as "::"

