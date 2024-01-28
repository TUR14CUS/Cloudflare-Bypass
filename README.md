# Automated Browsing using `undetected_chromedriver`

This Python script utilizes the `undetected_chromedriver` library to create an instance of the Chrome browser and navigate to a specified website. The `undetected_chromedriver` library helps in avoiding detection by websites that attempt to detect and block automated browser sessions.

## Features:

### 1. Automated Browsing:
   - Opens a new instance of Chrome using the `undetected_chromedriver`.
   - Takes the user input for the target website.
   - Navigates to the specified website.
   - Pauses for 10 seconds to simulate interaction or data retrieval.

### 2. Usage Instructions:

1. Install the required library:
   ```bash
   pip install undetected-chromedriver
   ```

2. Run the script using a Python interpreter.

3. Enter the URL of the website when prompted.

4. The script will open the Chrome browser, navigate to the specified website, and automatically close the browser after a 10-second pause.

## Usage Example:

```python
from undetected_chromedriver import Chrome
import time

# Create a new instance of Chrome using a context manager
with Chrome() as chrome:
    # Navigate to the website
    website = input("Enter the website: ")
    chrome.get(website)

    # Pause for 10 seconds (customize as needed)
    time.sleep(10)

# The browser will be closed automatically after exiting the 'with' block
```

**Note:**
- Customize the script based on your specific use case.
- Be aware of website terms of service and legal considerations when automating browsing.
- Use responsibly and ethically.
