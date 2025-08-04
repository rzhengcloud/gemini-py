import logging
import time

# --- Step 1: Basic Configuration (usually done once at the start of your application) ---

# Configure logging to write to a file and also to the console
# The 'level' sets the minimum severity level that will be processed.
# Messages below this level are ignored.
logging.basicConfig(
    level=logging.INFO, # Only INFO, WARNING, ERROR, CRITICAL messages will be shown
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"), # Send logs to app.log file
        logging.StreamHandler()        # Send logs to console (stderr by default)
    ]
)

# Get a logger instance. It's good practice to get a logger by name,
# typically the module's name (__name__).
logger = logging.getLogger(__name__)

# --- Step 2: Emitting Log Messages ---

def simulate_process(data):
    logger.debug(f"Starting simulate_process with data: {data}") # Won't show due to INFO level

    if not data:
        logger.warning("Input data is empty. Skipping processing.")
        return

    try:
        num_items = len(data)
        logger.info(f"Processing {num_items} items.")
        time.sleep(0.1) # Simulate some work

        if num_items < 5:
            logger.error("Too few items for efficient processing. Consider batching.")
            raise ValueError("Insufficient data.")

        result = sum(data) / num_items
        logger.info(f"Successfully processed data. Average: {result:.2f}")

    except ValueError as e:
        logger.exception("An error occurred during data processing!") # Logs ERROR + traceback
        # Instead of `logger.error("...", exc_info=True)`, logger.exception() is a shortcut
    except Exception as e:
        logger.critical(f"A critical unexpected error occurred: {e}")
        # Optionally re-raise if it's truly unrecoverable
        # raise

# --- How to use it ---

print("--- Testing Logging ---")

simulate_process([])
simulate_process([1, 2, 3])
simulate_process([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("\n--- Check 'app.log' file for full log output! ---")

# You can change the level dynamically for debugging purposes
logger.setLevel(logging.DEBUG) # Now DEBUG messages will also be shown
logger.debug("This DEBUG message will now appear!")