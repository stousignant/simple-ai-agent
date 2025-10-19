import os


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