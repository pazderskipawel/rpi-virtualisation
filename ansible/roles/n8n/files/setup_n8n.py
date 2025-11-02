#!/usr/bin/env python3
from playwright.sync_api import sync_playwright
import sys

def setup_n8n(url, email, first_name, last_name, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            # Navigate to setup page
            page.goto(url)
            page.wait_for_load_state('networkidle')
            
            # Fill the form (adjust selectors based on actual n8n form)
            page.fill('input[name="email"]', email)
            page.fill('input[name="firstName"]', first_name)
            page.fill('input[name="lastName"]', last_name)
            page.fill('input[name="password"]', password)
            
            # Click submit button
            page.click('button[type="submit"]')
            page.wait_for_timeout(2000)
            
            print("Setup completed successfully")
            browser.close()
            return 0
            
        except Exception as e:
            print(f"Error: {e}")
            browser.close()
            return 1

if __name__ == "__main__":
    setup_n8n(
        url=sys.argv[1],
        email=sys.argv[2],
        first_name=sys.argv[3],
        last_name=sys.argv[4],
        password=sys.argv[5]
    )
