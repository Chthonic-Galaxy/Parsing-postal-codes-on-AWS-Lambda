# Parsing-Postal-Codes-on-AWS-Lambda

This Python project leverages AWS Lambda, Playwright, and a postal code lookup website to extract postal codes for a given city. It's designed to be deployed as a serverless function on AWS Lambda.

**Functionality**

1. **User Input:** The script prompts the user to enter a city name.
2. **Web Automation:** It uses Playwright to automate interactions with the website [https://www.christopher-vogt.com/city2zip/](https://www.christopher-vogt.com/city2zip/), searching for postal codes based on the provided city name.
3. **Postal Code Extraction:** The script parses the resulting webpage to isolate the relevant postal codes.
4. **Output:** The extracted postal codes are neatly printed to the console.

**Dependencies**

* Playwright ([https://playwright.dev/](https://playwright.dev/))
* Chromium browser or a compatible executable

**Installation**

1. **Install Libs:**
   ```bash
   pip install -r requirements.txt
   ```
   
   or

   ```bash
   pip install playwright
   ```
2. **Download Chromium:** Playwright will automatically download Chromium on the first run. Or, download Chromium compatible with Playwright manually.

**Important Note:**

Ensure you have the correct Chromium executable path in the `executable_path` argument of the `p.chromium.launch()` line. You'll need to adjust this based on your installation location.

**Usage** 

* Once deployed on AWS Lambda, you can trigger the function. Input the desired city name to retrieve its postal codes.

**Disclaimer**

Please respect the terms of service of the website [https://www.christopher-vogt.com/city2zip/](https://www.christopher-vogt.com/city2zip/).  Avoid excessive scraping that could overload their servers.
