import json
from faker import Faker

# Initialize Faker
fake = Faker()

# Number of records to generate
num_records = 10**6

# File name for the output NDJSON file
file_name = "data.ndjson"

# Generate fake data and write to an NDJSON file
with open(file_name, "w") as file:
    for _ in range(num_records):
        # Create a fake data record
        data = {
            "name": fake.name(),
            "address": fake.address(),
            "email": fake.email(),
            "phone_number": fake.phone_number(),
            "company": fake.company(),
            "job": fake.job(),
            "date_of_birth": fake.date_of_birth().isoformat(),
        }

        # Write the record as a JSON object, followed by a newline
        file.write(json.dumps(data) + "\n")

print(f"Generated {num_records} fake data records and saved to {file_name}")
