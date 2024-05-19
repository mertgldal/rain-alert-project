# Rain Alert via SMS

## Description

This Python script checks the weather forecast using the OpenWeatherMap API. If rain is expected within the next few hours, it sends an SMS alert via Twilio.

## Prerequisites

- Python 3.x
- `requests` library
- `twilio` library
- `dotenv` library

## Setup

1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set up environment variables in a `.env` file:

```
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
OWM_API_KEY=your_openweathermap_api_key
MY_HOME_LAT=your_home_latitude
MY_HOME_LON=your_home_longitude
TWILIO_PHONE_NUM=your_twilio_phone_number
MY_PHONE_NUM=your_phone_number_to_receive_alerts
```

4. Run the script: `python rain_alert.py`.

## Usage

Run the script regularly to receive rain alerts via SMS for your specified location.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
