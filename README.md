# Prerequisites

- Python 3 installed
- API key for OpenWeatherMap API

## API Key
- Sign up for a free API key at https://home.openweathermap.org/users/sign_up
- After signing up, go to your profile page and copy your API key
- Set your API key as an environment variable named `OPEN_WEATHER_API_KEY`
    - `export OPEN_WEATHER_API_KEY=your_api_key_here`

# Steps to run the script

1. Clone the repository
2. Navigate to the project directory
3. Create a virtual environment (optional)
4. Install the required packages
    - `pip install -r requirements.txt`
5. Run the script
    - `python app.py`
6. Enter a valid zip or postal code e.g. 10001, 10002

# Example of response generated by this script

Enter zip code: 10001

Forecast for New York:

Date        Temperature     Precipitation
02/19/2023  47°/36°         0.00 in
02/20/2023  54°/44°         0.00 in
02/21/2023  51°/41°         1.31 in
02/22/2023  50°/35°         1.50 in
02/23/2023  42°/36°         4.28 in
02/24/2023  49°/42°         0.00 in



# Security best practices

- Keep sensitive information (such as API keys) out of the code.

- Instead, store them in a configuration file or environment variables. This can prevent others from viewing or using your sensitive information if they have access to your code.

- Use encryption when storing or transmitting sensitive data. For example, you can encrypt API key in the configuration file or use HTTPS when making API calls to ensure that data is transmitted securely.

- Validate user input to prevent malicious input or attacks. For example, you can use regular expressions to validate user input and ensure that it is in the expected format.

- Keep your code up to date with the latest security patches and best practices. This can help prevent known security vulnerabilities and protect your data from attacks.

