#!/usr/bin/env python3
from playwright.sync_api import sync_playwright
import sys

def setup_n8n(url, email, first_name, last_name, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to False to see browser
        page = browser.new_page()
        
        try:
            print(f"Navigating to {url}")
            page.goto(url)
            page.wait_for_load_state('networkidle')
            
            print("Page loaded, looking for form fields...")
            
            # Take a screenshot for debugging
            page.screenshot(path='/tmp/n8n_setup_before.png')
            print("Screenshot saved to /tmp/n8n_setup_before.png")
            
            # Print page content to see what's available
            print("Page title:", page.title())
            
            # Try to find and fill the form
            print(f"Filling email: {email}")
            page.fill('input[name="email"]', email)
            
            print(f"Filling first name: {first_name}")
            page.fill('input[name="firstName"]', first_name)
            
            print(f"Filling last name: {last_name}")
            page.fill('input[name="lastName"]', last_name)
            
            print(f"Filling password")
            page.fill('input[name="password"]', password)
            
            # Screenshot before submit
            page.screenshot(path='/tmp/n8n_setup_filled.png')
            print("Form filled, screenshot saved to /tmp/n8n_setup_filled.png")
            
            print("Clicking submit button")
            page.click('button[type="submit"]')
            page.wait_for_timeout(3000)
            
            # Screenshot after submit
            page.screenshot(path='/tmp/n8n_setup_after.png')
            print("After submit screenshot saved to /tmp/n8n_setup_after.png")
            
            print("Setup completed successfully")
            browser.close()
            return 0
            
        except Exception as e:
            print(f"Error: {e}")
            page.screenshot(path='/tmp/n8n_setup_error.png')
            print("Error screenshot saved to /tmp/n8n_setup_error.png")
            browser.close()
            return 1

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: setup_n8n.py <url> <email> <first_name> <last_name> <password>")
        sys.exit(1)
        
    setup_n8n(
        url=sys.argv[1],
        email=sys.argv[2],
        first_name=sys.argv[3],
        last_name=sys.argv[4],
        password=sys.argv[5]
    )
