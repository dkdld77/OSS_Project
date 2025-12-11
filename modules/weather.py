import requests

def get_weather(city="Seoul"):
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "날씨 정보 없음"
    except Exception as e:
        return f"에러 발생: {e}"

if __name__ == "__main__":
    print(get_weather())
