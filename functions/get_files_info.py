import os
#from ../config.py import FILE_CONTENT_CHARACTER_LIMIT
import config

def get_files_info(working_directory, directory="."):
    try:
        abs_working_dir = os.path.abspath(working_directory) 
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
        if not target_dir.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        directory_string = "current" if directory == "." else f"'{directory}'"
        result = f"Result for {directory_string} directory:"
        for file in os.listdir(target_dir):
            file_path = os.path.join(target_dir, file)
            result += f"\n - {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}"
        return result
    except Exception as e:
        return f"Error: {e}"


def get_file_content(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        if not target_file_path.startswith(abs_working_dir):
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(target_file_path) or os.path.isdir(target_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_file_path, "r") as f:
            file_content_string = f.read(config.FILE_CONTENT_CHARACTER_LIMIT)
            if len(file_content_string) >= config.FILE_CONTENT_CHARACTER_LIMIT:
                file_content_string += f"[...File \"{file_path}\" truncated at 10000 characters]"
            return file_content_string
    except Exception as e:
        return f'Error: {e}'
        