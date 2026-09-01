"""
Time Zone Converter

Tells the user the current time in a different city, given their
local time and the two locations. See ANSWERS_T7.md for the
assumptions and research behind this solution.
"""

CITY_OFFSETS = {
    "london": 0,
    "new york": -5,
    "tokyo": 9,
    "sydney": 10,
    "dubai": 4,
    "paris": 1,
}


def get_offset(city_name):
    """Return the UTC offset in hours for city_name, or None if unknown."""
    return CITY_OFFSETS.get(city_name.lower())


def convert_time(hour, minute, from_city, to_city):
    """Return the (hour, minute) time in to_city, given a time in from_city."""
    from_offset = get_offset(from_city)
    to_offset = get_offset(to_city)

    difference = to_offset - from_offset
    total_minutes = hour * 60 + minute + difference * 60
    total_minutes = total_minutes % (24 * 60)

    new_hour = total_minutes // 60
    new_minute = total_minutes % 60
    return new_hour, new_minute


def main():
    print("Supported cities:", ", ".join(city.title() for city in CITY_OFFSETS))
    from_city = input("Your city: ")
    to_city = input("City you want the time for: ")
    time_input = input("Your local time (HH:MM): ")

    hour, minute = time_input.split(":")
    hour = int(hour)
    minute = int(minute)

    if get_offset(from_city) is None or get_offset(to_city) is None:
        print("Sorry, one of those cities isn't supported yet.")
        return

    new_hour, new_minute = convert_time(hour, minute, from_city, to_city)
    print(f"It is {new_hour:02d}:{new_minute:02d} in {to_city.title()}.")


if __name__ == "__main__":
    main()
