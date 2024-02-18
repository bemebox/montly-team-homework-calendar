import requests
from datetime import datetime
from collections import namedtuple

# create constant values
Constants = namedtuple("Constants", ["public_holidays_base_url", "country_code"])
constants = Constants("https://date.nager.at/api/v3/PublicHolidays", "PT")


def main():
    # get current date
    current_date = get_current_date()

    # get current month country public holidays
    month_public_holidays_by_month = get_country_public_holidays_by_month(
        constants.country_code, current_date.year, current_date.month
    )


def get_country_public_holidays_by_month(country_code, year, month):
    """
    get public holidays for a specific country, year, and month.

    Args:
        country_code (str): the ISO country code (e.g., 'US', 'GB').
        year (int): the year for which to retrieve public holidays.
        month (int): the month for which to retrieve public holidays (1 to 12).

    Returns:
        list: a list of public holidays for the specified country, year, and month.
              each holiday is represented as a dictionary with date, year, month, day, and description.

    Example:
        get_country_public_holidays_by_month('US', 2024, 7)
    """
    month_holidays = []

    year_country_public_holidays = get_country_public_holidays_by_year(
        country_code, year
    )
    if year_country_public_holidays:
        for holiday in year_country_public_holidays:
            public_holiday_date = datetime.strptime(holiday["date"], "%Y-%m-%d")
            if public_holiday_date.month == month:
                month_holidays.append(
                    {
                        "date": holiday["date"],
                        "year": public_holiday_date.year,
                        "month": public_holiday_date.month,
                        "day": public_holiday_date.day,
                        "description": holiday["localName"],
                    }
                )

    return month_holidays


def get_country_public_holidays_by_year(country_code, year):
    """
    get public holidays for a specific country and year, from an external API.

    Args:
        country_code (str): the ISO country code (e.g., 'US', 'GB').
        year (int): the year for which to retrieve public holidays.

    Returns:
        list or None: a list of public holidays for the specified country and year.
                      returns None if the request fails.

    Example:
        get_country_public_holidays_by_year('US', 2024)
    """
    endpoint = f"{constants.public_holidays_base_url}/{year}/{country_code}"

    response = requests.get(endpoint)

    if response.status_code == 200:
        holidays = response.json()
        return holidays
    else:
        print(f"Failed to retrieve holidays. Status Code: {response.status_code}")
        return None


def get_current_date():
    """
    function that get the current date.

    Returns:
        datetime.date: the current date.
    """
    # get the current date and time
    current_date_time = datetime.now()

    # return the current date
    return current_date_time.date()


if __name__ == "__main__":
    main()
