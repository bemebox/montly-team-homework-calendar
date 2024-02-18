from datetime import datetime


def main():
    # get current date
    current_date = get_current_date()


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
