# Simple AI Agent

Simple AI Agent is a command-line interface (CLI) tool that leverages Google's Gemini AI model to perform coding tasks autonomously. This project demonstrates the implementation of an AI agent with function calling capabilities, allowing the model to interact with the file system, execute Python code, and perform various file operations within a secure, sandboxed environment.

## Tech Stack

-   **Language**: Python 3.12+
-   **AI Model**: Google Gemini 2.5 Flash
-   **Dependencies**: `google-genai` (AI client), `python-dotenv` (environment configuration)
-   **Tooling**: uv (package management)

## Features

-   **Function Calling**: The AI agent can autonomously call functions to accomplish tasks:
    -   **File Reading**: Read file contents from the working directory (with character limits for large files).
    -   **File Listing**: List files and directories to explore the project structure.
    -   **Code Execution**: Execute Python files with optional command-line arguments.
    -   **File Writing**: Create or overwrite files within the working directory.
-   **Security**: All operations are restricted to a configurable working directory, preventing access to files outside the designated scope.
-   **Iterative Problem Solving**: The agent can make multiple function calls in sequence, allowing it to explore, understand, and modify codebases to complete complex tasks.
-   **Verbose Mode**: Optional verbose output for debugging, showing function calls, token usage, and detailed execution information.
-   **Configurable**: Simple configuration through environment variables and constants for model selection, iteration limits, and working directory.

## Achievements & Key Learnings

Building this Simple AI Agent provided valuable experience in:
-   **Function Calling Architecture**: Implementing a robust function calling system that allows an AI model to interact with the system through well-defined schemas and secure execution boundaries.
-   **Conversation Management**: Designing a conversation loop that handles multi-turn interactions, function calls, and responses, ensuring the agent can iteratively work toward a solution.
-   **Security & Sandboxing**: Developing path validation logic to ensure all file operations remain within a designated working directory, preventing unauthorized access to the broader filesystem.
-   **Error Handling**: Creating comprehensive error handling for file operations, subprocess execution, and API interactions to provide meaningful feedback when operations fail.
-   **CLI Development**: Building a user-friendly command-line interface that accepts natural language prompts and provides clear output.

## Getting Started

### Prerequisites

-   **Python** (3.12+ recommended)
-   **uv** (package manager)
-   **Google Gemini API Key** (get one from [Google AI Studio](https://makersuite.google.com/app/apikey))

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/yourusername/simple-ai-agent.git
    cd simple-ai-agent
    ```

2.  Install dependencies:
    ```bash
    uv sync
    ```

3.  Set up environment variables:
    Create a `.env` file in the project root:
    ```bash
    echo "GEMINI_API_KEY=your_api_key_here" > .env
    ```

### Usage

To use the AI agent, run the main script with a natural language prompt:

```bash
python main.py "<your_prompt>"
```

**Options:**
-   `--verbose`: Enable verbose output showing function calls, token usage, and detailed execution information.

**Examples:**

```bash
# Simple task
python main.py "List all files in the calculator directory"

# Complex task with verbose output
python main.py --verbose "Read the calculator.py file and explain what it does"

# Code execution task
python main.py "Run the calculator.py file with arguments 5 and 3"
```

The agent will:
1.  Process your prompt using the Gemini AI model.
2.  Make function calls as needed to gather information or perform actions.
3.  Iterate until it can provide a final response or complete the requested task.
4.  Display the results in the terminal.

### Configuration

You can customize the agent's behavior by modifying `constants.py` and `config.py`:

-   `GEMINI_MODEL`: The Gemini model to use (default: `"gemini-2.5-flash"`).
-   `MAX_ITERATIONS`: Maximum number of function calling iterations before timeout (default: `20`).
-   `WORKING_DIR`: The directory where file operations are permitted (default: `"./calculator"`).
-   `MAX_CHARS`: Maximum characters to read from a file (default: `10000`).

## Available Functions

The agent has access to the following functions:

1.  **`get_file_content(file_path)`**: Reads and returns the content of a file.
2.  **`get_files_info(directory_path)`**: Lists files and directories in the specified path.
3.  **`run_python_file(file_path, args=None)`**: Executes a Python file with optional command-line arguments.
4.  **`write_file(file_path, content)`**: Writes or overwrites a file with the provided content.

All paths are relative to the configured working directory for security.

## Running Tests

To run the test suite:

```bash
python -m pytest
```

Or run individual test files:

```bash
python test_get_file_content.py
python test_get_files_info.py
python test_run_python_file.py
python test_write_file.py
```

## Output

The agent provides output in the following format:

-   **Function Calls**: Each function call is displayed with its name and parameters (or just the name in non-verbose mode).
-   **Function Results**: The results of function calls are shown, including any errors.
-   **Final Response**: The agent's final answer or completion message.

In verbose mode, you'll also see:
-   Token usage statistics (prompt tokens and response tokens).
-   Detailed function call parameters.
-   Full function response content.

---
*This project was built as part of the backend engineering curriculum at [Boot.dev](https://www.boot.dev/).*
