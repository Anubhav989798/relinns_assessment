import openai
import requests
from bs4 import BeautifulSoup

openai.api_key = "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" 

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    content_element = soup.find(class_='container') 

    if content_element:
        extracted_info = content_element.get_text()
        return extracted_info
    else:
        print("Error: Content element not found on the webpage.")
        return ""

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

def main():
    website_url = "https://www.relinns.com"  
    extracted_info = scrape_website(website_url)
    processed_info = extracted_info.split(". ")  

    print("welcome please submit your query")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        prompt = f"You: {user_input}\nWeb Data: {processed_info}\nChatbot:"

        response = generate_response(prompt)
        print(response)

if __name__ == "__main__":
    main()
