import requests


class ApiError(Exception):
    pass


def get_request(endpoint):
    """
    perform a GET request to the specified endpoint.

    Parameters:
    - endpoint (str): the URL endpoint to send the GET request to.

    Returns:
    - dict or None: if the request is successful (status code 200), return the JSON content.
                   otherwise, raise an ApiError or return None based on the encountered error.

    Raises:
    - ApiError: custom exception for API-related errors, with specific messages based on HTTP status codes.
    """
    if endpoint:
        response = requests.get(endpoint)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise ApiError(f"Error: Resource not found at {endpoint}")
        elif response.status_code == 500:
            raise ApiError(f"Error: Internal Server Error at {endpoint}")
        else:
            raise ApiError(
                f"Error: Unexpected status code {response.status_code} at {endpoint}"
            )

    # Handle the case when the endpoint is not provided or other generic errors
    raise ApiError(f"Error: Unable to fetch data from {endpoint}")
