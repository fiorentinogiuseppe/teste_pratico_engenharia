from intUtilx.utils import create_connection, load_json, close_client

# Creat connection with default parameters
my_collection, client = create_connection()

# Load file with default parameters
file_data = load_json()

# Insert json in database
my_collection.insert_many(file_data)

# Closing connection
close_client(client)
