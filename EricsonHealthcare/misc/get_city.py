from bs4 import BeautifulSoup
import pdb, requests

with open(r"C:\Users\Divyam Shah\OneDrive\Desktop\Dynamic Labz\Clients\Clients\Ericson Healthcare\Ericson-Healthcare\EricsonHealthcare\misc\city.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse HTML
soup = BeautifulSoup(html_content, "html.parser")

# Extract sections
sections = soup.find_all("section", {"data-level": "1"})

state_city_mapping = {}

for section in sections:
    try:
        # Extract state name
        state_name = section.find("h2").find("a").text.strip()
        # pdb.set_trace()

        # Extract city names properly
        cities = [a.text.strip() for a in section.find_all("li")]

        # Store in dictionary
        state_city_mapping[state_name] = cities
    
    except Exception as e:
        print(f"Error occurred: {e}")
        pdb.set_trace()

def send_city(city, state):
    url = "http://127.0.0.1:8000/custom-admin-add-visit"

    response = requests.get(url, params={"city": city, "state": state})
    print(response.json())


pdb.set_trace()
# Print result
for state, cities in state_city_mapping.items():
    print(f"State: {state} ---------------------------------")
    for city in cities:
        print(f"City: {city}")
        send_city(city, state)
    print("Cities:", ", ".join(cities) if cities else "No cities found")
    print("-" * 30)
