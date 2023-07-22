import requests
from plyer import notification

# Function to fetch the top news headlines
def get_top_headlines():
    api_key = '1eab62c255b34f6dab9121ca27482c3a'  # Replace with your News API key
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'ok':
        articles = data['articles']
        headlines = [article['title'] for article in articles]
        return headlines
    else:
        return []

# Function to display desktop notifications
def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Display the notification for 10 seconds
    )

# Get top news headlines
headlines = get_top_headlines()

if headlines:
    # Display each headline as a desktop notification
    for headline in headlines:
        show_notification('Top News Headline', headline)
else:
    show_notification('Error', 'Failed to fetch news headlines')
