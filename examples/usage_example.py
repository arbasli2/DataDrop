from finally_data_logger import DataLogger
import numpy as np

# Initialize the client
client = DataLogger()

# Reset the database for a fresh start
client.reset_database()

# Create a random numpy image for demonstration purposes
img = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

# Logging data with different attributes
data_entries = [
    {"name": "test1", "duration": 0.3, "PSNR": 51.0, "image": img},
    {"name": "test1", "duration": 0.4, "PSNR": 50.0, "image": img},
    {"name": "testN", "duration": 0.5, "PSNR": 50.0, "image": img},
]

for data in data_entries:
    response = client.log_data(data)
    print(response)

# Fetch all data entries with name containing "test"
results = client.get_data({"name": "test*"}, fetch_blob=True)
print(f"Number of fetched results: {len(results)}")

# Modify the last logged data entry's name and image
client.modify_data(results[-1]["entry_id"], {"name": "test2", "image": img})

# Fetch all data entries again to confirm the modification
results_updated = client.get_data({"name": "*"}, fetch_blob=True)
print(f"Number of fetched results after modification: {len(results_updated)}")

# Define criteria for deletion and delete matching data
criteria = {"duration": 0.4}
response = client.delete_data(criteria)
print(response)
