import time
import main

if __name__ == "__main__":
    # Record the start time
    start_time = time.time()

    # Call the main function
    main()

    # Calculate the runtime
    end_time = time.time()
    runtime = end_time - start_time

    print(f"Script executed in {runtime:.2f} seconds.")
