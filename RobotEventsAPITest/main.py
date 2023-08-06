import requests
import json

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

endpoint = "https://www.robotevents.com/api/v2/events?start=2023-08-05T21%3A10%3A49.247Z&myEvents=false"
extension = "&page="

original_response = requests.get(endpoint, auth=BearerAuth('')).json()
total_response = []

page_nums = int(original_response['meta']['last_page'])
for i in range(page_nums+1):
    if(i == 0):
        continue
    else:
        endpoint = endpoint + extension + str(i)
        current_response = requests.get(endpoint, auth=BearerAuth('')).json()
        print(current_response['meta']['current_page'])
        total_response.append(current_response)

for item in total_response:
    print(json.dumps(item, indent=2))

#formatted_string = json.dumps(response.json(), indent=2)
#print(formatted_string)
#eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiMzAzYWVkMDQzNTE0MjQ4M2E3YjgxNDYyMjM2ZTA4MGI0ZmFkNGZmMTRlNjJkYmQwMjQ3NTQ4ZGY3NGEyMjQyNmQxYjU5MjhmYzEwZjVmMjQiLCJpYXQiOjE2OTEwNzcxODUuODQ1Mjg4LCJuYmYiOjE2OTEwNzcxODUuODQ1MjkwOSwiZXhwIjoyNjM3ODUxOTg1LjgzOTY3MjEsInN1YiI6IjExNjkxMyIsInNjb3BlcyI6W119.lOVJp5mafwW25QEQRinSxrkL4kKFQLuzAy3pRjbi6jzzB6uBYzamq7NuAowI18Wvf8jM5WyjowXSjX9_V4vEfUCeHJIo1Bs6SvntEy0vodLh0oF_hbXm49ZBqlmOnbyUdPeas3nW0-iwMs_wKwgEtEsndP87FXYkkh8sjhrzYWXm7xOFUX7bn66-IIFYndDxmubIlEknuYXzGuEHPOVLY1ydaPBO0ylcmCa0Uzh5grFai29ssosF8IMOm_xXDT4oiQmLocnMR2EjUAZ_dw6BdNl0lHd96nuGVWyQ4usjPdZVKliNeviQILLtgPV3Tg2k6G5OTfoCGQoREUMUAnYpVq8F0QD7XjRUIgWanrahHAt-VAgOt_wuN0EwFznTCaGlLolMBk630vYfpbM6blevQNIYEv9kyJlTbofISmU-B-D_Ui4li2P7fteliWKBvxp5CFnLMIWu9nyTut_uH17B9l4-rLd4JqxJE2a-u2Qr05drn9YXdCd_e5TFDT10ZmLvs51O1aC0ozuYrkKQFzQZnR7eZkgRci1AEFbGiQN3HvxkXeUazwMRke-ZIYMzv08W7VwqimdanAYhb6TQfd3vWuw0-UCu3vsmlxeXjBOfYO0L-nPWX6ZgYA61h7CNM3mzXeNRy_7PD-XoQOjWVzYOptzjzVuC_mdMFbSeO3i3DEw

