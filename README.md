# Dual-Mode AI Assistant

A sophisticated chatbot that can switch between emotional support and logical reasoning modes using LangGraph and the Groq API with Gemma-2 9B model.

## Features

- **Dynamic Mode Switching**: Automatically classifies user input as either emotional or logical
- **Emotional Support Mode**: Acts as a compassionate therapist for emotional queries
- **Logical Mode**: Provides fact-based, analytical responses for information-seeking queries
- **State Management**: Uses LangGraph for efficient conversation state handling

## Prerequisites

- Python 3.8+
- Groq API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install required packages:
```bash
pip install dotenv langgraph langchain openai pydantic requests typing-extensions
```

3. Create a `.env` file in the project root and add your Groq API key:
```
GROQ_API_KEY=your_api_key_here
```

## Usage

Run the main chatbot:
```bash
python agent.py
```

Enter your messages when prompted. Type 'exit' to end the conversation.

## How It Works

1. **Message Classification**: Each user input is analyzed by the classifier to determine if it requires an emotional or logical response.

2. **Router**: Based on the classification, the message is routed to either:
   - Therapist Agent: For emotional support and empathetic responses
   - Logical Agent: For fact-based and analytical responses

3. **Response Generation**: The appropriate agent processes the message and generates a contextually relevant response.

## Project Structure

- `agent.py`: Main implementation with state management and routing logic
- `main.py`: Simplified version of the chatbot
- `.env`: Contains API key (not tracked in git)
- `.gitignore`: Specifies files to ignore in version control

## License

[Your chosen license]

## Contributing

[Your contribution guidelines]