import requests
from bs4 import BeautifulSoup
import json

class InstaRecentImages():

    def scrap_insta(self, username):
        images = []
        
        try:
            if username:
                url = "https://www.instagram.com/" + username
            else:
                print("Please provide username")

            response = requests.get(url)

            soup = BeautifulSoup(response.text)
            print(soup)

            scripts = soup.find_all("script", {'type': 'text/javascript'})

            for script in scripts:
                content = script.get_text()
                if content.startswith('window._sharedData = '):
                    content = content.replace("window._sharedData = ", "")
                    if content.endswith(';'):
                        content = content[:-1]

                    insta_data = json.loads(content)
                    posts = insta_data.get('entry_data', {}).get('ProfilePage', [{}])[0].get('graphql', {}).get('user', {}).get('edge_owner_to_timeline_media').get('edges', {})

                    count = 0
                    for post in posts:
                        if count == 3:
                            break

                        image = post.get('node', {}).get('thumbnail_src')
                        images.append(image)
                        count += 1
        except:
            pass

        return images





def main():
    # my code here
    username = "bala_07_dhoni"
    I = InstaRecentImages()

    print(I.scrap_insta(username))


if __name__ == "__main__":
    main()


