import requests

def test_price_agent():
    try:
        response = requests.get("http://localhost:8000/price")
        print("Price response:", response.json())
    except Exception as e:
        print("Error sending message to Price:", e)

def test_news_agent():
    try:
        response = requests.get("http://localhost:8001/news")
        print("News response:", response.json())
    except Exception as e:
        print("Error sending message to News:", e)

def test_alert_agent():
    try:
        response = requests.get("http://localhost:8002/alert")
        print("Alerts response:", response.json())
    except Exception as e:
        print("Error sending message to Alerts:", e)

def test_assistant_agent():
    try:
        response = requests.get("http://localhost:8003/assistant", params={"message": "What is the price of BTC and crypto news?"})
        print("Agent response:", response.json())
    except Exception as e:
        print("Error sending message to Agent:", e)

def test_all_agents():
    test_price_agent()
    test_news_agent()
    test_alert_agent()
    test_assistant_agent()

if __name__ == "__main__":
    test_all_agents()