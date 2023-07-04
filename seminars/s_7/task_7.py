# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

# groups = {
#             Path('video'): ['avi', 'mkv'],
#             Path('image'): ['jpg', 'png'],
#         }

# def create_file(path, ext, name):
#     save_path = path
#     if ext in ['bin', 'dll']:
#         save_path += "/bin"
#     elif ext in ['jpg', 'png', 'jpeg']:
#         save_path += "/images"
#     elif ext in ['pdf', 'doc', 'txt']:
#         save_path += "/text"
#     else:
#         save_path += "misc"
#     if not os.path.exists(save_path):
#         os.makedirs(save_path)
#     with open(f"{save_path}/{name}.{ext}", "wb") as f:
#         f.write(randbytes(255))

