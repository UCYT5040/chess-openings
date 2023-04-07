import json
import os

import fire
import grequests
import requests


def merge_responses(responses: list):
    """
    Merges all the responses into one json file
    :param responses:
    :return:
    """
    items = []
    for r in responses:
        items.extend(r.json()["items"])
    return {"items": items}


def main(seperate_pages: bool=False):
    """
    Downloads all the openings from chess.com
    :param mergePages: If true, all the pages will be merged into one json file, otherwise, each page will be saved in a separate file
    :return:
    """
    API_URL = "https://www.chess.com/callback/eco/advanced-search?keyword=&useFavorites=false&page="
    r = requests.get(f"{API_URL}1")
    total_pages = r.json()["page_range"]
    urls = [API_URL + str(i) for i in range(1, total_pages + 1)]
    rs = (grequests.get(u) for u in urls)
    responses = grequests.map(rs)
    responses.insert(0, r)
    if not seperate_pages:
        if not os.path.exists("pages"):
            os.makedirs("pages")
        for r in responses:
            with open(f"pages/page_{r.json()['current_page_number']}.json", "w") as f:
                f.write(r.text)
    else:
        with open("openings.json", "w") as f:
            json.dump(merge_responses(responses), f)


if __name__ == "__main__":
    fire.Fire(main)
