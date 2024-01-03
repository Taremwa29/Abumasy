from app.init import app
import os

def clear_pycache(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".pyc"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted: {file_path}")

if __name__ == "__main__":
    application_directory = '/Abumasy'
    clear_pycache(application_directory)
    print("PyCache cleared successfully.")
    app.run(debug= True)
