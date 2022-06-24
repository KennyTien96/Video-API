import requests

BASE = "http://127.0.0.1:5000/"

# data = [{"name" : "Kenny", "views" : 1000000, "likes" : 357},
#         {"name" : "How to make REST API", "views" : 1000000, "likes" : 100075},
#         {"name" : "Best Food in NYC" , "views" : 1000000, "likes" : 357},
#         ]
#
# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())


# input()
# response = requests.patch(BASE + "video/2", {"views" : 99, "likes" : 5})
# print(response.json())

# response = requests.get(BASE + "video/2")
# print(response.json())

response = requests.delete(BASE + "video/2")
print(response)
