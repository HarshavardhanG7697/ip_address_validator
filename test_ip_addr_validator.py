import unittest
import ip_addr_validator


class TestIpAddrValidator(unittest.TestCase):
    def test_valid_ipv4(self):
        self.assertTrue(ip_addr_validator.is_valid_ipv4("0.0.0.0"))
        self.assertFalse(ip_addr_validator.is_valid_ipv4("0.0.0"))

    def test_valid_ipv6(self):
        self.assertTrue(ip_addr_validator.is_valid_ipv6("::"))
        self.assertTrue(ip_addr_validator.is_valid_ipv6("0:0:0:0:0:0:0:0"))
        self.assertFalse(ip_addr_validator.is_valid_ipv6("0:0:0:0:0:0:0:0:0"))
        self.assertFalse(ip_addr_validator.is_valid_ipv6("0"))
        self.assertFalse(ip_addr_validator.is_valid_ipv6(":"))


if __name__ == "__main__":
    unittest.main()
