# # with open("my_file.txt", 'r') as f:
# #     for line in f.readlines():
# #         print(line)


# # with open("my_file.txt", 'w') as f:
# #     for i in range(1_000_000):
# #         f.write(f"This is line {i+1}.\n")



# def get_file(file_name):
#     with open(file_name, 'r') as f:
#         all_lines = f.readlines() # <-- THIS IS THE KEY PART: loads everything!
#         print(f"Successfully loaded {len(all_lines)} lines into memory.")
#         # for line in f.readlines():
#         #     yield line

# line=0
# if __name__ == "__main__":
#     file_name = "my_file.txt"
#     get_file(file_name)
#     # for x in get_file(file_name):
#     #     if (line+1) % 10_000 == 0:
#     #         print(x)
#     #     line+=1



import os
import time

def create_dummy_large_file(filename="large_log.txt", num_lines=5_000_000):
    """Creates a dummy text file with a specified number of lines."""
    print(f"Creating {filename} with {num_lines} lines...")
    start_time = time.time()
    with open(filename, "w") as f:
        for i in range(num_lines):
            f.write(f"This is line number {i + 1} of the log file, which is fairly long to increase memory footprint.\n")
    end_time = time.time()
    print(f"Finished creating {filename} in {end_time - start_time:.2f} seconds.")

def process_all_lines_at_once(filepath):
    """
    Reads ALL lines from a file into memory at once and then processes them.
    This is the method that will cause a memory spike for large files.
    """
    print(f"\n--- Processing '{filepath}' by loading all lines into memory ---")
    start_time = time.time()
    try:
        with open(filepath, 'r') as file:
            all_lines = file.readlines() # <-- THIS IS THE KEY PART: loads everything!
            print(f"Successfully loaded {len(all_lines)} lines into memory.")

            line_count = 0
            for line in all_lines:
                # Simulate processing (e.g., stripping whitespace)
                processed_line = line.strip()
                if line_count % 500000 == 0:
                    print(f"  Processing (all-at-once) line {line_count + 1}: {processed_line[:50]}...")
                line_count += 1
            print(f"Finished processing {line_count} lines (all-at-once).")

    except MemoryError:
        print(f"!!! MemoryError: The file '{filepath}' is too large to load all at once. !!!")
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        end_time = time.time()
        print(f"Total time for all-at-once processing: {end_time - start_time:.2f} seconds.")


def process_lines_with_generator(filepath):
    """
    A generator function that reads lines from a file one by one,
    without loading the entire file into memory, and yields them.
    """
    def read_lines_lazy(inner_filepath):
        try:
            with open(inner_filepath, 'r') as file:
                for line in file:
                    yield line.strip()
        except FileNotFoundError:
            print(f"Error (generator): The file '{inner_filepath}' was not found.")
            return # Terminate generator
        except Exception as e:
            print(f"An error occurred (generator): {e}")
            return # Terminate generator

    print(f"\n--- Processing '{filepath}' using a generator (yield) ---")
    start_time = time.time()
    line_count = 0
    for processed_line in read_lines_lazy(filepath):
        # Simulate processing
        if line_count % 500000 == 0:
            print(f"  Processing (generator) line {line_count + 1}: {processed_line[:50]}...")
        line_count += 1
    print(f"Finished processing {line_count} lines (generator).")
    end_time = time.time()
    print(f"Total time for generator processing: {end_time - start_time:.2f} seconds.")


if __name__ == "__main__":
    file_name = "large_log.txt"
    # Create a large dummy file first.
    # Adjust num_lines based on your system's RAM.
    # 5 million lines is a good starting point for a test,
    # but for very constrained systems, you might need less (e.g., 1M).
    # For a definite MemoryError on most systems, try 50,000,000+ lines.
    create_dummy_large_file(file_name, num_lines=5_000_000)

    # --- Run the "all at once" version first to observe the spike ---
    print("\n----- Running 'process_all_lines_at_once' -----")
    # Add a short delay here so you have time to start monitoring after the print statement
    time.sleep(2)
    process_all_lines_at_once(file_name)
    time.sleep(5) # Give time for memory to potentially deallocate, though Python's GC is not immediate

    # --- Then run the "generator" version ---
    print("\n----- Running 'process_lines_with_generator' -----")
    time.sleep(2)
    process_lines_with_generator(file_name)

    # Clean up the dummy file
    print(f"\nCleaning up {file_name}...")
    os.remove(file_name)
    print("Done.")