import requests

API_KEY = "b753d850e0c578eb4cc97e7a13f35423"


def get_data(place, forecast_days=None):
    """Get data from the open weather API.
    The open weather API needs an API key.
    """
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Singapore", forecast_days=1))