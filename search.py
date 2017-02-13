from googleapiclient.discovery import build
import pprint
import io, json

my_api_key = "AIzaSyCst6-blNSpMRFV2ElB7d4SCbsvXRio6zI"
my_cse_id = "008848616393262483149:bhspvm4pely"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search('sydney australia', my_api_key, my_cse_id, num=10)


with io.open('sydney_data.txt', 'w', encoding='utf-8') as f:
	f.write(unicode(json.dumps(results, ensure_ascii=False)))

# results = google_search('crude oil site:www.bloomberg.com/news/articles/', my_api_key, my_cse_id, num=5)
# for result in results:
#     # pprint.pprint(result)
#     print result['title']
#     print result['snippet']


