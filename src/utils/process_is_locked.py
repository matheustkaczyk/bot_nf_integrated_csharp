import psutil

def is_file_locked(file_path):
    """Check if a file is locked by another process."""
    for proc in psutil.process_iter():
        try:
            for file in proc.open_files():
                if file.path == file_path:
                    return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False