# Currency Converter Chatbot

## Overview
The Currency Converter Chatbot is a real-time currency conversion service with chatbot functionality, available for seamless interaction via Telegram. The chatbot integrates advanced features such as real-time exchange rates, user-friendly interaction, and robust API integrations, making currency conversion effortless for users.

**Telegram Bot Link**: [Convert My Currency Bot](https://t.me/convert_my_currency_bot)

---

## Features
- **Real-Time Currency Conversion**: Get up-to-date currency conversion rates.
- **Chatbot Interface**: Interact through a simple and intuitive Telegram bot.
- **Accurate Responses**: Powered by reliable APIs and verified testing.

---

## Technologies Used

### Languages and Frameworks
- **Python**
- **Flask**: Backend framework for building the web application.

### APIs
- **Currency Conversion API**: Provides real-time exchange rate data.

### Hosting and Deployment
- **Vercel**: Flask app hosted for seamless availability and scalability.

### Development Tools
- **Ngrok**: Enabled webhook integration during development.
- **Postman**: Used for testing API responses.
- **Dialogflow**: Designed and implemented the chatbot’s conversational flow.

---

## Installation and Setup

### Prerequisites
1. Python 3.7+
2. `pip` package manager
3. Telegram account

### Steps to Set Up Locally
1. Clone the repository:
   ```bash
   git clone <repository-link>
   ```

2. Navigate to the project directory:
   ```bash
   cd currency-converter-chatbot
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the `APIKEY` file:
   - Create a file named `APIKEY.py` in the root directory.
   - Add your API key:
     ```python
     apiKey = "YOUR_API_KEY"
     ```

5. Run the Flask app:
   ```bash
   python app.py
   ```

6. Use Ngrok to expose your local server to the internet:
   ```bash
   ngrok http 5000
   ```

7. Configure Dialogflow webhook to point to the Ngrok URL.

---

## Usage
1. Open the Telegram bot using the provided link.
2. Interact with the bot by sending currency conversion queries, e.g., "Convert 100 USD to INR."
3. The bot responds with the real-time converted value.

---

## Testing
- Use Postman to send POST requests to the Flask app and verify API responses.
- Example POST request body:
  ```json
  {
    "queryResult": {
      "parameters": {
        "unit-currency": {
          "currency": "USD",
          "amount": 100
        },
        "currency-name": "INR"
      }
    }
  }
  ```

---

## Resources and Acknowledgments
- **Dialogflow**: [Official Documentation](https://cloud.google.com/dialogflow/docs)
- **Currency Conversion API**: [API Documentation](https://currencyapi.com/)
- **CampusX YouTube Channel**: Learn more about the project and related tutorials from [CampusX](https://www.youtube.com/c/CampusXOfficial).

---

## Future Scope
- Add support for multiple languages.
- Integrate additional financial tools and features.

---


