import os
import shutil

def delete_files(file_paths):
    for file_path in file_paths:
        try:
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")

def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f"Deleted folder: {folder_path}")
    except FileNotFoundError:
        print(f"Folder not found: {folder_path}")
    except Exception as e:
        print(f"Error deleting folder {folder_path}: {e}")

def clean_up():
    folders_to_delete = ['YoutubeAudios', 'converted_images', 'classified_text']
    files_to_delete = ['combined_text.txt']

    for folder in folders_to_delete:
        delete_folder(folder)
    
    for file in files_to_delete:
        delete_files([file])

# if __name__ == "__main__":
#     clean_up()
