import requests
import os
# url = "https://api.telegram.org/bot7339245446:AAFSjoEhDrnqlFuVGoxWcYykykqJ4qRjPso/setWebhook?remove="
#
# payload = { "url": "" }
# headers = {
#     "accept": "application/json",
#     "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
#     "content-type": "application/json"
# }
#
# response = requests.post(url, json=payload, headers=headers)
#
# print(response.text)

BOT_TOKEN = os.getenv('BOT_TOKEN')
FILE_ID = os.getenv('FILE_ID')


# Step 1: Get the file path
get_file_url = f'https://api.telegram.org/bot{BOT_TOKEN}/getFile?file_id={FILE_ID}'
response = requests.get(get_file_url)
file_info = response.json()

print("File Info Response:", file_info)  # Debugging information

if file_info['ok']:
    file_path = file_info['result']['file_path']
    print("File Path:", file_path)  # Debugging information

    # Step 2: Download the file
    download_url = f'https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}'
    print("Download URL:", download_url)  # Debugging information

    file_response = requests.get(download_url, stream=True)

    # Check if the request was successful
    if file_response.status_code == 200:
        # Save the file locally
        with open('downloaded_video.mp4', 'wb') as file:
            for chunk in file_response.iter_content(chunk_size=8192):
                file.write(chunk)
        print("Video downloaded successfully!")
    else:
        print("Failed to download the file. Status code:", file_response.status_code)
else:
    print("Failed to get file info.")