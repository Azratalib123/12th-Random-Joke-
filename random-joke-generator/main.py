import streamlit as st  # for creating the web app
import requests  # for making HTTP requests to the API
import random  # for selecting random fallback jokes

def get_random_joke():
    """Fetch a random joke from the API"""
    try:
        # Make GET request to joke API
        response = requests.get("https://official-joke-api.appspot.com/random_joke")

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            joke_data = response.json()
            # Return formatted joke with setup and punchline (dictionary keys)
            return f"😂 {joke_data['setup']} \n\n 🤣 {joke_data['punchline']}"
        else:
            # Return error message if API call fails
            return "😢 Oops! Couldn't fetch a joke. Try again later."
    except:
        # Return fallback joke if exception occurs like internet issues
        fallback_jokes = [
            "🤖 Why do programmers prefer dark mode? \n Because light attracts bugs!",
            "📸 How does a computer get drunk? \n It takes screenshots!",
            "👓 Why do Java developers wear glasses? \n Because they don't C#!"
        ]
        return random.choice(fallback_jokes)

def main():
    """Main function to run the Streamlit app"""
    # Set page title
    st.title("😂 Random Joke Generator 🤣")
    # Add instruction text
    st.write("Click the button below to generate a random joke 😆")

    # Create button and handle click
    if st.button("🎲 Generate Joke 🎭"):
        # Get random joke when button clicked
        joke = get_random_joke()
        # Display joke with success styling
        st.success(joke)

    # Add horizontal line
    st.divider()

    # Footer using HTML, displaying text in the center
    st.markdown(
        """
    <div style='text-align:center;'>
        <p>🎤 Joke from Official Joke API</p>
        <p>Built with ❤️ by <a href='https://github.com/Azratalib123'>Azra Talib</a> using Streamlit 🚀</p>
    </div>
    """,
        unsafe_allow_html=True
    )

# Run main function when script is executed directly
if __name__ == "__main__":
    main()
