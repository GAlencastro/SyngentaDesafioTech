import re
import numpy as np
from collections import OrderedDict

# Dictionary with information about prices according to both types of guests, rating and names
HOTELS_INFO = {
    'names': ['Lakewood', 'Bridgewood', 'Ridgewood'],
    'rates': [3, 4, 5],
    'daily_values': {
        'business_days': {
            'regular': np.array([110.0, 160.0, 220.0]),
            'rewards': np.array([80.0, 110.0, 100.0]),
        },
        'weekend_days': {
            'regular': np.array([90.0, 60.0, 150.0]),
            'rewards': np.array([80.0, 50.0, 40.0]),
        },

    }
}


# Main function to test prices and return the cheapest hotel during the given days
def get_cheapest_hotel(inputString: str) -> str:
    info_reservation = filter_line(inputString)
    cheapest_hotel = evaluate_minimum_price(**get_infos(info_reservation))
    print(cheapest_hotel)
    return cheapest_hotel


# Function to evaluate all the prices and return lowest one. In case of a tie, return the hotel with more rating
# Returns name of the cheapest hotel
def evaluate_minimum_price(
        num_business_days: int,
        num_weekend_days: int,
        guest_type: str,
) -> str:
    prices = num_business_days * HOTELS_INFO['daily_values']['business_days'][guest_type] + \
             num_weekend_days * HOTELS_INFO['daily_values']['weekend_days'][guest_type]

    best_hotels_idx = np.where(prices == np.min(prices))
    rates_masked = np.array(HOTELS_INFO['rates'], dtype=int)[best_hotels_idx]
    hotels_masked = np.array(HOTELS_INFO['names'])[best_hotels_idx]

    return hotels_masked[np.argmax(rates_masked)]


# Function for filtering the input string about the guest, getting the type of guest,
# number of days and their types (business or weekend days).
# Returns list with first index always informing type of guest
def filter_line(line: str) -> list:
    r = re.compile(r'\bRegular\b | \bRewards\b | \bmon\b | \btues\b | \bwed\b |'
                   r' \bthur\b | \bfri\b | \bsat\b | \bsun\b',
                   flags=re.I | re.X)
    tmp = np.array(r.findall(line))
    info_reservation = list(np.char.lower(tmp))
    return info_reservation


# Function to consolidate the information about the guest, counting how many days each day type has.
# Returns a dictionary with guest type, number of each day type
def get_infos(line_info: list[str]) -> dict:
    infos = OrderedDict()
    infos['guest_type'] = line_info[0]

    infos['num_weekend_days'] = line_info.count('sun') + line_info.count('sat')
    infos['num_business_days'] = len(line_info) - infos['num_weekend_days'] - 1

    return infos
