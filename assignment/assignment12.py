
# import requests
# print("***RHYMING WORD GENERATOR*****")
# a=input("enter a sentence:")
# endpoint = f"https://api.datamuse.com/words?ml={a}"
# response = requests.get(endpoint)
# data = response.json()
# if response.status_code == 200:
#     for item in data:
#         print(item.get('tags'))


# import requests
# print("***RHYMING WORD GENERATOR*****")
# a=input("enter a sentence:")
# endpoint = f"https://api.datamuse.com/words?rel_jjb={a}"
# response = requests.get(endpoint)
# data = response.json()
# if response.status_code == 200:
#     for item in data:
#         if item.get('score')>950:
#             print(f"{item.get('word')} score:{item.get('score')}")
