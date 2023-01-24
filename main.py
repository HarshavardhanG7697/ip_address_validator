#!/Users/hv/Documents/GitHub/ip_addr_validator/.venv/bin/python3
import logging

logging.basicConfig(format='%(asctime)s-[%(levelname)s]-%(message)s', 
datefmt='%H:%M:%S %d-%m-%Y',
level=logging.INFO
)

HEXADECIMALS = "0123456789abcdefABCDEF"

# Function to validate IPv4 addresses
def is_valid_ipv4(given_ip_addrr) -> bool:
    logging.info("validating if the ip address is ipv4")
    split_ip_address = given_ip_addrr.split(".")
    logging.debug(f"split: {split_ip_address}")
    if len(split_ip_address) == 4:
        logging.debug("the given ip address has 4 octets as expected.")
        if all([int(octet) <= 255 for octet in split_ip_address]):
            logging.info("each octet is between 0 - 255")
            logging.info(f"ip address {given_ip_addrr} is a valid IPv4 address.")
            return True
        else:
            logging.warning("the octets do not lie between 0 - 255")
            logging.warning(f"ip address {given_ip_addrr} is invalid.")
            return False
    else:
        logging.warning("number of octets is not equal to 4")
        logging.warning(f"ip address {given_ip_addrr} is invalid.")
        return False

# Function to validate IPv6 address
def is_valid_ipv6(given_ip_addrr) -> bool:
    logging.info("validating if the ip address is ipv6")
    split_ip_address = given_ip_addrr.split(":")
    logging.debug(f"split: {split_ip_address}") 
    if len(split_ip_address) > 2 and len(split_ip_address) <= 8:
        logging.debug("ip address has more than 3 and less than 8 segments.")
        logging.debug([segment[i] for segment in split_ip_address for i in range(len(segment))])
        logging.debug([segment[i] in HEXADECIMALS for segment in split_ip_address for i in range(len(segment))])
        if all([segment[i] in HEXADECIMALS for segment in split_ip_address for i in range(len(segment))]):
            logging.info("each value in each segment is a hexadecimal")
            if all([len(segment) <= 4 for segment in split_ip_address]):
                logging.debug("length of each segment is less than 4")
                logging.info(f"ip address {given_ip_addrr} is a valid ipv6 address")
                return True
            else:
                logging.warning("length of each segment is greater than 4")
                logging.warning(f"ip address {given_ip_addrr} is invalid")
                return False
        else:
            logging.warning("each value in each segment is not a hexadecimal")
            logging.warning(f"ip address {given_ip_addrr} is invalid")
            return False
    else:
        logging.warning("ip address has incorrect number segments.")
        logging.warning(f"ip address {given_ip_addrr} is invalid")
        return False


ip_address = input("Enter the IP address you would like to vaidate: ")

try:
    try:
        if "." in ip_address:
            if is_valid_ipv4(ip_address):
                logging.info("valid IPv4 address")
        else:
            raise ValueError("ip address is not a ipv4.")
    except ValueError as e:
        logging.error(e)
        if ":" in ip_address:
            if is_valid_ipv6(ip_address):
                logging.info("valid IPv4 address")
        else:
            logging.error("ip address is not a ipv6.")
            raise TypeError("input is not a valid string")
except TypeError as e:
    logging.warning(e)
    logging.critical("Make sure that the IP address entered is a string.")