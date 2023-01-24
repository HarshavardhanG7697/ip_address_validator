#!/Users/hv/Documents/GitHub/ip_addr_validator/.venv/bin/python3

import logging

logging.basicConfig(format='%(asctime)s-[%(levelname)s]-%(message)s', 
datefmt='%H:%M:%S %d-%m-%Y ',
level=logging.INFO
)

ip_address = "255.255.255.255"
# Function to validate IPv4 addresses
def is_valid_ipv4(given_ip_addrr) -> bool:
    logging.debug("Validating if the ip address is ipv4")
    split_ip_address = given_ip_addrr.split(".")
    logging.debug(split_ip_address)
    if len(split_ip_address) == 4:
        logging.debug("The given ip address has 4 octets as expected.")
        if all([int(octet) <= 255 for octet in split_ip_address]):
            logging.info("Each octet is between 0 - 255")
            logging.info(f"IP address {given_ip_addrr} is a valid IPv4 address.")
            return True
        else:
            logging.warning("The octets do not lie between 0 - 255")
            logging.warning(f"IP address {given_ip_addrr} is invalid.")
            return False
    else:
        logging.warning("Number of octets is not equal to 4")
        logging.warning(f"IP address {given_ip_addrr} is invalid.")
        return False

try:
    logging.info(is_valid_ipv4(ip_address))
except:
    logging.warn("invalid IP")