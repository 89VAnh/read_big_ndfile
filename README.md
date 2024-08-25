## Overview

1. **`fake.py`**: Generates a large NDJSON file with fake data.
2. **`read_data.py`**: Splits a large NDJSON file into smaller chunks and processes each chunk in parallel.

## Files

### `fake.py`

This script generates a large NDJSON file with fake data records. 

#### Features
- Uses the `Faker` library to create fake data.
- Generates a specified number of records (default is 1 million).
- Saves the data to a file named `data.ndjson`.

#### Usage
1. Ensure you have the `Faker` library installed:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the script:
    ```bash
    python fake.py
    ```

### `read_data.py`

This script splits a large NDJSON file into smaller chunks and processes them in parallel using multiprocessing.

#### Features
- Splits the NDJSON file into 2GB chunks.
- Processes each chunk using 8 parallel worker processes.
- Cleans up chunk files after processing.

#### Usage
1. Place the `data.ndjson` file in the same directory as the script.
2. Run the script:
    ```bash
    python read_data.py
    ```
