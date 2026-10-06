# Chatbot Using Langchain

## About the Project

This project is a chatbot application built with Streamlit and LangChain. It accepts a user question in a web interface, sends it to an OpenAI model through LangChain, and displays the model's response directly in the browser.

The app loads the OpenAI API key from a local `.env` file and uses the `langchain_openai` package to initialize the chat model.

## Tech Stack

- Python
- Streamlit
- LangChain
- OpenAI API
- python-dotenv

## Features

- Simple Streamlit-based chat interface
- Reads the API key from `.env`
- Creates a LangChain OpenAI chat model
- Sends user input to the model
- Displays the generated response in the app

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/varadshinde2505/Chatbot-using-Langchain.git
cd Chatbot-using-Langchain
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

- Windows:
  ```bash
  .venv\Scripts\activate
  ```
- macOS/Linux:
  ```bash
  source .venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your OpenAI API Key

Create a `.env` file in the project's root directory:

```env
OPENAI_API_KEY=your-api-key
```

### 5. Run the App

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal in your browser.

## App Behavior

The `app.py` file:

- loads the `.env` file from the same directory as the script
- reads `OPENAI_API_KEY`
- checks whether the key exists
- creates a `ChatOpenAI` model instance
- takes a text input from the user
- calls `llm.invoke(query)`
- displays the result using `st.write()`

## Example

A sample query you can enter in the app:

```text
Explain how LangChain helps build AI applications.
```

The app sends this query to the configured model and shows the response below the input box.

## Notes

- Make sure your `.env` file is not committed to public repositories.
- The app currently uses `ChatOpenAI(model="gpt-6-luna")`, so ensure the model name matches the model available to your OpenAI account.

## License

This project is open source and available under the MIT License.
