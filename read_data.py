import json
import multiprocessing
import os
import gc

def process_chunk(chunk_path):
    """Process a chunk of data from the file."""
    with open(chunk_path, "r") as f:
        for line in f:
            data = json.loads(line)
            # Process data
    gc.collect()  # Free up memory after processing

def split_file_by_size(file_path, chunk_size):
    """Split a large file into smaller chunks based on size."""
    chunk_paths = []
    with open(file_path, "r") as f:
        chunk_count = 0
        chunk_lines = []
        current_size = 0
        for line in f:
            chunk_lines.append(line)
            current_size += len(line.encode("utf-8"))
            if current_size >= chunk_size:
                chunk_path = f"chunk_{chunk_count}.ndjson"
                with open(chunk_path, "w") as chunk_file:
                    chunk_file.writelines(chunk_lines)
                chunk_paths.append(chunk_path)
                chunk_lines = []
                current_size = 0
                chunk_count += 1
        if chunk_lines:
            chunk_path = f"chunk_{chunk_count}.ndjson"
            with open(chunk_path, "w") as chunk_file:
                chunk_file.writelines(chunk_lines)
            chunk_paths.append(chunk_path)
    return chunk_paths

def main():
    file_path = "data.ndjson"
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return
    
    ndjson_size = os.path.getsize(file_path)
    num_worker = 8
    chunk_size = 2 * (1024 ** 3)  # Size of each chunk is 2GB

    # Split the large file into smaller chunks
    chunk_paths = split_file_by_size(file_path, chunk_size)

    # Use multiprocessing to process chunks in parallel
    with multiprocessing.Pool(processes=num_worker) as pool:
        pool.map(process_chunk, chunk_paths)

    # Remove chunk files after processing
    for chunk_path in chunk_paths:
        os.remove(chunk_path)

if __name__ == "__main__":
    main()