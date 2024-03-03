import asyncio
from playwright.async_api import async_playwright

async def extract_postcodes(city_name):
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=r"path\to\chromium") # Replace with the path to your Chromium executable
        page = await browser.new_page()
        await page.goto('https://www.christopher-vogt.com/city2zip/')

        # Input the city name
        city_input = await page.query_selector('#city_data')
        await city_input.type(city_name)

        # Submit the form
        search_button = await page.query_selector('#search_button')
        await search_button.click()

        await page.wait_for_selector('.plz')

        # Extract postcodes
        postcodes = await page.evaluate('''() => {
            const plzElements = document.querySelectorAll('.plz');
            return Array.from(plzElements).map(el => el.textContent.trim());
        }''')

        await browser.close()
        return postcodes

if __name__ == '__main__':
    city_name = input("Enter city name: ")
    postcodes = asyncio.run(extract_postcodes(city_name))

    print("Postcodes for", city_name, ":", postcodes) 
