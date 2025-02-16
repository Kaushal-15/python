import requests
# Replace 'your_api_key_here' with your actual API key
API_KEY = ''

def get_ai_response(base_url, prompt):
    """
    Fetches AI-generated responses from the provided API endpoint.
    
    Args:
        base_url (str): The API URL to send the request.
        prompt (str): The input prompt for the AI.

    Returns:
        str: The AI's response or an error message.
    """
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    
    data = {
        "prompt": prompt,
        "max_tokens": 150,
        "temperature": 0.7
    }

    try:
        response = requests.post(base_url, headers=headers, json=data)
        response.raise_for_status()  # Raise error for HTTP codes 4xx/5xx
        return response.json().get('data', {}).get('text', 'No response text available.')
    except requests.exceptions.RequestException as e:
        return f"Request error: {e}"
    except ValueError:
        return "Error parsing response JSON."

def main():
    print("Welcome to AI Code Buddy!")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting AI Code Buddy. Goodbye!")
            break
        
        # Ask user for the API URL
        api_url = input("Enter the full API URL (or press Enter to use default): ").strip()
        if not api_url:
            print("Error: API URL is required!")
            continue

        ai_response = get_ai_response(api_url, user_input)
        print(f"AI Code Buddy: {ai_response}")

if __name__ == "__main__":
    main()


