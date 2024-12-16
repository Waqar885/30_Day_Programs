import threading
import time, os
import requests

def download(address, file):
    url = address

    file_name = f'100 day coding/30_Programs/ Programs 24/images/{file}.jpg'


    try:
        response = requests.get(url)
        response.raise_for_status() # Automatically raises an error for bad responses


        with open(file_name, 'wb') as image:
            image.write(response.content)

        print(f"File downloaded successfully as '{file_name}'")

    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return
    


while True:
    choice = input('Enter 1 for download per image\n2 for download more than one\n3 to exit: ')
    if choice == '1':
        link = input('Enter link of image: ').strip()
        name = input('Enter file name you want to save it: ')
        p = threading.Thread(target=download, args=[link, name])
        p.start()

    elif choice == '2':
        address = input('Enter file address: ')
        images = []
        with open(address, 'r') as links:
            lines = links.readlines()
        t1 = time.perf_counter()
        for i, line in enumerate(lines):
            p = threading.Thread(target=download, args=[line, i])
            p.start()
            images.append(p)
        
        # Wait for all threads to complete
        for thread in images:
            thread.join()
        
        t2 = time.perf_counter()
        print(f'Time ⏰ taken for download is {t2 - t1} seconds')

    elif choice == '3':
        break

    else:
        print('Please enter between 1-3')
