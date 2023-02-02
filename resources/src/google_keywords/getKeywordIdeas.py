from google.ads.googleads.client import GoogleAdsClient
import generate_keyword_ideas as gki


location_ids = ["2840", "2826"]  # 2840 is for United States

language_id = "1000"  # 1000 is for English

keywords = ['travel destinations']
page_url = 'https://tripadvisor.com'
site_url = None


client = GoogleAdsClient.load_from_dict(credentials)

list_keywords = gki.main(
    client, customer_id, location_ids, language_id, keywords, page_url, site_url)

filtered_keywords = []
for keyword in list_keywords:
    if (keyword.keyword_idea_metrics.avg_monthly_searches > 10000):
        filtered_keywords.append(keyword)

for idea in filtered_keywords:
    competition = idea.keyword_idea_metrics.competition
    competition_index = idea.keyword_idea_metrics.competition_index

    print(
        f'Keyword idea text "{idea.text}" has '
        f'"{idea.keyword_idea_metrics.avg_monthly_searches}" '
        f'average monthly searches and "{competition}" '
        f'competition_index and "{competition_index}" '
        "competition.\n"
    )
# print(list_keywords)
