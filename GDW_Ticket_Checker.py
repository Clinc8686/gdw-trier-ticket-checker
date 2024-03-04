import requests

def search_for_string(url, search_string):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text

        if search_string in html_content:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Zugriff auf die Seite: {e}")

url = "https://www.eventbrite.de/e/gamedevweek-2024-tickets-688739998877"
search_string = "Ausverkauft"
discord_webhook = ""
discord_parameter = {'content': '@everyone **Es gibt GameDevWeek Trier 2024 Tickets!**'}

if search_for_string(url, search_string) == False:
    requests.post(discord_webhook, discord_parameter)
