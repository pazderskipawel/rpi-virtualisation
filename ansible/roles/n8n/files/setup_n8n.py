#!/usr/bin/env python3
from playwright.sync_api import sync_playwright
import sys

def setup_n8n(url, email, first_name, last_name, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            print(f"Navigating to {url}")
            page.goto(url)
            page.wait_for_load_state('networkidle')
            
            # Fill the form fields
            print(f"Filling email: {email}")
            page.fill('input[name="email"]', email)
            
            print(f"Filling first name: {first_name}")
            page.fill('input[name="firstName"]', first_name)
            
            print(f"Filling last name: {last_name}")
            page.fill('input[name="lastName"]', last_name)
            
            print(f"Filling password")
            page.fill('input[name="password"]', password)
            
            # Click the "Next" button using data-test-id
            print("Clicking Next button")
            page.click('button[data-test-id="form-submit-button"]')
            
            # Wait for navigation/success
            page.wait_for_timeout(3000)
            
            page.screenshot(path='/tmp/n8n_setup_after.png')
            print("Setup completed successfully")
            browser.close()
            return 0
            
        except Exception as e:
            print(f"Error: {e}")
            page.screenshot(path='/tmp/n8n_setup_error.png')
            print("Error screenshot saved to /tmp/n8n_setup_error.png")
            print("User might be already set up!!!")
            browser.close()
            return 0

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: setup_n8n.py <url> <email> <first_name> <last_name> <password>")
        sys.exit(1)
        
    sys.exit(setup_n8n(
        url=sys.argv[1],
        email=sys.argv[2],
        first_name=sys.argv[3],
        last_name=sys.argv[4],
        password=sys.argv[5]
    ))
