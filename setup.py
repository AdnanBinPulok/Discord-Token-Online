import os

# send command to install requirmenets.txt
os.system('pip install -r requirements.txt')

import shutil
from git import Repo
import stat
import errno
from tempfile import TemporaryDirectory




def handle_remove_readonly(func, path, exc_info):
    exc_type, exc_value, exc_tb = exc_info
    if exc_type is PermissionError and exc_value.errno == errno.EACCES:
        os.chmod(path, stat.S_IRWXU)
        func(path)
    else:
        raise

def download_and_keep_folder(repo_url, folder_name, destination='./'):
    # Create a temporary directory to clone the repository
    with TemporaryDirectory() as temp_dir:
        try:
            Repo.clone_from(repo_url, temp_dir)
        except Exception as e:
            return
        
        # Define the source and destination paths for the folder to keep
        src_folder = os.path.join(temp_dir, folder_name)
        dest_folder = os.path.join(destination, folder_name)
        
        # Ensure the destination directory exists
        if not os.path.exists(destination):
            os.makedirs(destination)
        
        # If the destination folder already exists, remove it
        if os.path.exists(dest_folder):
            shutil.rmtree(dest_folder, onerror=handle_remove_readonly)
        
        # Move the folder to the destination
        if os.path.exists(src_folder):
            shutil.move(src_folder, dest_folder)

# Example usage
download_and_keep_folder('https://github.com/dolfies/discord.py-self.git', 'discord', './')
