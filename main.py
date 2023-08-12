from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't request website")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    # "html.parser" tells Beautifulsoup to send HTML.
    jobs = soup.find_all("section", class_="jobs")
    # Find all the section that have the class of jobs.
    # class_="jobs" is keyword argument.
    for job_section in jobs:
        job_posts = job_section.find_all("li")
        job_posts.pop(-1)
        # pop method is for removing view-all list, it is located on the last of the list.
        for post in job_posts:
            print(post)
            print("//////////////")
