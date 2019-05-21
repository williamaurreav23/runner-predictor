import requests
from bs4 import BeautifulSoup


class EnduhubFetcher:
    """Responsible for download results from enduhub"""

    def __init__(self, runner_name, birth_year):
        self.runner_name = runner_name
        self.birth_year = birth_year
        self.number_of_pages = 0
        self.pages_content = {}
        self.race_results = []

    def __str__(self):
        return "{}, {}".format(self.runner_name, self.birth_year)

    def fetch_results(self):
        for page in range(1, self.number_of_pages + 1):
            content = self.download_page(page)
            soup = BeautifulSoup(content, "html.parser")
            for row in soup.find_all("tr", class_="Zawody"):
                event_name = row.find("td", class_="event").get_text()
                distance = row.find("td", class_="distance").get_text()
                race_date = row.find("td", class_="date").get_text()
                runner_birth = row.find("td", class_="yob").get_text()
                result_of_the_race = row.find("td", class_="best").get_text()
                race_type = row.find("td", class_="sport").get_text()
                race_result = dict(
                    race_name=event_name,
                    distance=distance,
                    race_date=race_date,
                    runner_birth=runner_birth,
                    result_of_the_race=result_of_the_race,
                    race_type=race_type,
                )
                self.race_results.append(race_result)

        return self.race_results

    def prepare_web_links(self):
        page_number = 1
        content = self.download_page(page_number)
        self.pages_content[page_number] = content
        soup = BeautifulSoup(content, "html.parser")
        pagination_li_a = soup.select(".pagination .pages li a")
        uniq_links = set([a_tag["href"] for a_tag in pagination_li_a])
        self.number_of_pages = len(uniq_links)

    def download_page(self, page):
        page_content = self.pages_content.get(page)
        if page_content:
            return page_content
        link_template = "https://enduhub.com/pl/search/?name={}&page={}"
        print("prepare_donwload", link_template)
        r = requests.get(link_template.format(self.runner_name, page))
        return r.content
