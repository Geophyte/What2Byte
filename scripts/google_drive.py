from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()           
drive = GoogleDrive(gauth)


def upload_files(upload_file_list: list, folder_id: str):
    """
    zapisuje podane pliki do folderu na drive'ie
    jesli chcemy by zapisal np recipes.json musimy podac data/recipes.json
    od razu zapisze tez pod nazwa data/recipes.json, 
    tak aby przy pobieraniu z powrotem od razu zapisal sie do odpowiedniego folderu
    """
    for upload_file in upload_file_list:
        gfile = drive.CreateFile({'parents': [{'id': folder_id}]})
        gfile.SetContentFile(upload_file)
        gfile.Upload()


# def get_file_list(folder_id: str):
#     files = {}
#     file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(folder_id)}).GetList()
#     for file in file_list:
#         files[file['title']] = file['id']
#     return files


# def get_file_content(folder_id, file_name):
#     files = get_file_list(folder_id)
#     file_id = files[file_name]
#     file = drive.CreateFile({'id': file_id})
#     file.GetContentString(file_name)


def get_files(folder_id):
    """
    pobiera wszystkie pliki z folderu
    (zapisuje do odpowiedniego folderu, np data/recipes.json zapisze do folderu data jako recipes.json)
    """
    file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(folder_id)}).GetList()
    for file in file_list:
        file.GetContentFile(file['title'])


def create_folder():
    """
    tworzy w drive'ie folder do ktorego beda zapisywane dane
    tworzy plik z id tego folderu
    zwraca id
    """
    gfile = drive.CreateFile({'title': 'What2Byte', 'mimeType': 'application/vnd.google-apps.folder'})
    gfile.Upload()
    id = gfile['id']
    f = open("data/folder_id.txt", "a")
    f.write(id)
    f.close()
    return id


def get_folder_id():
    """
    zwraca id folderu z pliku
    """
    f = open("data/folder_id.txt", "r")
    return f.read()
