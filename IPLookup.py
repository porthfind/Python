from ipwhois import IPWhois
from ipwhois.utils import get_countries

def validate_ip(ip):
    if ip.count('.') == 3:
        return True
    else:
        return False


def ip_lookup(ip):

    countries = get_countries()
    a = IPWhois(ip)
    results = a.lookup(False)
    print("It belongs to: %s"%countries[results['nets'][0]['country']])

def main():
    ip = input("Please insert an IP:")

    if validate_ip(ip):
        ip_lookup(ip)
    else:
        print("That was not a valid IP")


if __name__ == "__main__":
    main()
