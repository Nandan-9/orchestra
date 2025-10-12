# Install supabase client if not already
# pip install supabase

from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv("SUPPUBASE_URL")
SUPABASE_KEY = os.getenv("SUPPUBASE_KEY")

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Path to your local video file

def upload_to_storage(scene_name, file_path):


    # Storage bucket name
    bucket_name = "orchestra"

    try:
        # Open the file in binary mode
        with open(file_path, "rb") as file:
            data = file.read()

        # Upload to Supabase Storage
        response = supabase.storage.from_(bucket_name).upload(scene_name, data)

        print("Upload successful!")
        print("File info:", response)
        return response

    except Exception as e:
        print("Error uploading file:", e)
