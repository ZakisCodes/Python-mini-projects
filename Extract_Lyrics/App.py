api_key = "AIzaSyB46ntHNwGF1oRo1mzCPoAp50AtvOG0n68"
api_custom = "AIzaSyB46ntHNwGF1oRo1mzCPoAp50AtvOG0n68"
engine_id = "b149a829c1d784d37"
import requests
"""from lyrics_extractor import SongLyrics
extract_lyrics = SongLyrics(api_key,engine_id)
data = extract_lyrics.get_lyrics("Brothers and Sisters")

print(data["lyrics"])"""
API_KEY = api_key
SEARCH_ENGINE_ID = engine_id
query = "shape of you"
url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}"
params = {'num': 10, 'start': 2}
starts = list(x for x in range(1,100,10))
for start in starts :
    API_KEY = api_key
    SEARCH_ENGINE_ID = engine_id
    query = "corona"
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}"
    res = requests.get(url, params=params).json()
    print(res)