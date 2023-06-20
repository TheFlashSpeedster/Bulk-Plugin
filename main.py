import re
import requests

def extract_links(input_url, output_file, excluded_extensions):
    response = requests.get(input_url)
    text = response.text

    links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    
    filtered_links = [link for link in links if not any(extension in link for extension in excluded_extensions)]
    
    with open(output_file, 'w') as file:
        file.write('\n'.join(filtered_links))

    print(f"✅ Links Extracted")

# Example usage
input_url = input("📤 Enter Direct Link of TXT File: ")
output_file = 'ace.txt'
excluded_extensions = ['.html', '.srt', '.txt', '.png', '.jpg', '.jpeg', '.url', '.nfo', '.webp']  # Add the extensions you want to exclude in this list

extract_links(input_url, output_file, excluded_extensions)

# Upload the file to file.io
file_io_url = 'https://file.io'
files = {'file': open(output_file, 'rb')}
response = requests.post(file_io_url, files=files)

# Get the URL for accessing the file
download_url = response.json()['link']

print("📝 Conversion Completed 🎉")
print(f"📩 Download: {download_url}")
