import requests
from bs4 import BeautifulSoup

def scrape_github_profile(url):
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve profile from {url}")
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract profile name
    name_tag = soup.find('span', class_='p-name vcard-fullname d-block overflow-hidden')
    profile_name = name_tag.text.strip() if name_tag else 'N/A'
    
    # Extract username
    username_tag = soup.find('span', class_='p-nickname vcard-username d-block')
    profile_username = username_tag.text.strip() if username_tag else 'N/A'
    
    # Extract bio
    bio_tag = soup.find('div', class_='p-note user-profile-bio mb-3 js-user-profile-bio f4')
    profile_bio = bio_tag.text.strip() if bio_tag else 'N/A'
    
    # Extract location
    location_tag = soup.find('li', class_='vcard-detail pt-1 css-truncate css-truncate-target')
    profile_location = location_tag.text.strip() if location_tag else 'N/A'
    
    # Extract repositories count
    repos_tag = soup.find('span', class_='Counter')
    repos_count = repos_tag.text.strip() if repos_tag else 'N/A'
    
    profile_info = {
        'Name': profile_name,
        'Username': profile_username,
        'Bio': profile_bio,
        'Location': profile_location,
        'Repositories': repos_count
    }
    
    return profile_info

if __name__ == "__main__":
    url = "https://github.com/Nelzouki22"
    profile_info = scrape_github_profile(url)
    
    if profile_info:
        print("Profile Information:")
        for key, value in profile_info.items():
            print(f"{key}: {value}")

