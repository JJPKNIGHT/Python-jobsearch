import re
import requests

def search_glassdoor(job_title, location):
    url = f'https://www.glassdoor.com/Job/jobs.htm?sc.keyword={job_title}&locT=C&locId=10&locKeyword={location}&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=all&remoteWorkType=all'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    response = requests.get(url, headers=headers)
    html_content = response.text

    # Using regex to extract job titles and companies
    jobs = re.findall(r'<a class="jobLink".*?>(.*?)</a>.*?<div class="d-flex flex-wrap css-11d3uq0">(.*?)</div>', html_content, re.DOTALL)

    print(f"Glassdoor: Found {len(jobs)} Director of Product Management jobs in Canada")
    for job in jobs:
        title = job[0].strip()
        company = re.sub(r'<.*?>', '', job[1]).strip()
        print(f"Title: {title}, Company: {company}")

def search_linkedin(job_title, location):
    url = f'https://www.linkedin.com/jobs/search/?keywords={job_title}&location={location}&sortBy=DD'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    response = requests.get(url, headers=headers)
    html_content = response.text

    # Using regex to extract job titles and companies
    jobs = re.findall(r'<span class="screen-reader-text">(.*?)</span>.*?<h4 class="base-search-card__subtitle">(.*?)</h4>', html_content, re.DOTALL)

    print(f"LinkedIn: Found {len(jobs)} Director of Product Management jobs in Canada")
    for job in jobs:
        title = job[0].strip()
        company = job[1].strip()
        print(f"Title: {title}, Company: {company}")

def main():
    job_title = input("Enter job title: ")
    location = input("Enter location: ")

    search_glassdoor(job_title, location)
    search_linkedin(job_title, location)

if __name__ == "__main__":
    main()