# import json
# with open('user.json', 'r', encoding='utf-8') as f:
# json_file = json.load(f)
# print(f'{type(json_file) = }\n{json_file = }')
# print(f'{json_file["name"] = }')
# print(f'{json_file["address"]["geo"] = }')
# print(f'{json_file["email"] = }')
#
# import json
# json_text = """
# [
# {
# "userId": 1,
# "id": 9,
# "title": "nesciunt iure omnis dolorem tempora et
# accusantium",
# "body": "consectetur animi nesciunt iure dolore"
# },
# {
# "userId": 1,
# "id": 10,
# "title": "optio molestias id quia eum",
# "body": "quo et expedita modi cum officia vel magni"
# },
# {
# "userId": 2,
# "id": 11,
# "title": "et ea vero quia laudantium autem",
# "body": "delectus reiciendis molestiae occaecati non minima
# eveniet qui voluptatibus"
# },
# {
# "userId": 2,
# "id": 12,
# "title": "in quibusdam tempore odit est dolorem",
# "body": "praesentium quia et ea odit et ea voluptas et"
# }
# ]"""
# print(f'{type(json_text) = }\n{json_text = }')
# json_list = json.loads(json_text)
# print(f'{type(json_list) = }\t{len(json_list) = }\n{json_list = }')
#
# import json
# my_dict = {
# "first_name": "Джон",
# "last_name": "Смит",
# "hobbies": ["кузнечное дело", "программирование",
# "путешествия"],
# "age": 35,
# "children": [
# {
# "first_name": "Алиса",
# "age": 5
# },
# {
# "first_name": "Маруся",
# "age": 3
# }
# ]
# }
# print(f'{type(my_dict) = }\n{my_dict = }')
# with open('new_user.json', 'w') as f:
# json.dump(my_dict, f)
#
# my_dict = {
# "first_name": "Джон",
# "last_name": "Смит",
# "hobbies": ["кузнечное дело", "программирование",
# "путешествия"],
# "age": 35,
# "children": [
# {
# "first_name": "Алиса",
# "age": 5
# },
# {
# "first_name": "Маруся",
# "age": 3
# }
# ]
# }
# dict_to_json_text = json.dumps(my_dict)
# print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')
#
# my_dict = {
# "id": 123,
# "name": "Clementine Bauche",
# "username": "Cleba",
# "email": "cleba@corp.mail.ru",
# "address": {
# "street": "Central",
# "city": "Metropolis",
# "zipcode": "123456"
# },
# "phone": "+7-999-123-45-67"
# }
# res = json.dumps(my_dict, indent=2, separators=(',', ':'),
# sort_keys=True)
# print(res)
#
import pickle

data = b'\x80\x04\x95\xe3\x00\x00\x00\x00\x00\x00\x00}\x94(' \
       b'\x8c\nfirst_name\x94\x8c\x08\xd0\x94\xd0\xb6\xd0\xbe\xd0\xbd\x94\x8c\tlast_name\x94\x8c\x08\xd0\xa1\xd0\xbc' \
       b'\xd0\xb8\xd1\x82\x94\x8c\x07hobbies\x94]\x94(' \
       b'\x8c\x1b\xd0\xba\xd1\x83\xd0\xb7\xd0\xbd\xd0\xb5\xd1\x87\xd0\xbd\xd0\xbe\xd0\xb5 ' \
       b'\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xbe\x94\x8c\xd0\xbf\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0' \
       b'\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5\x94\x8c\x16\xd0\xbf\xd1\x83\xd1\x82\xd0\xb5\xd1' \
       b'\x88\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd1\x8f\x94e\x8c\x03age\x94K#\x8c\x08children\x94]\x94(}\x94(' \
       b'h\x01\x8c\n\xd0\x90\xd0\xbb\xd0\xb8\xd1\x81\xd0\xb0\x94h\nK\x05u}\x94(' \
       b'h\x01\x8c\x0c\xd0\x9c\xd0\xb0\xd1\x80\xd1\x83\xd1\x81\xd1\x8f\x94h\nK\x03ueu.'
new_dict = pickle.loads(data)
print(f'{new_dict = }')
