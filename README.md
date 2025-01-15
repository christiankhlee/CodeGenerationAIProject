# CodeGenerationAIProject
AI-Powered Code Generation and Documentation Tool
This project uses Cohere's API to generate Python code snippets and corresponding documentation based on natural language descriptions. The tool allows users to input a simple description of a coding task, and the model returns both the Python code and an auto-generated docstring for the code. It aims to enhance productivity by automating repetitive tasks and improving code documentation.

Features
Code Generation: Automatically generates Python code based on a given natural language prompt.
Documentation Generation: Creates docstrings for the generated Python code, explaining its functionality, parameters, and return values.
Simple User Interface: Users provide a description (e.g., "Generate a Python function to sort a list of dictionaries by key"), and the tool returns the generated code and documentation.
Technologies Used
Python: The core programming language for the tool.
Cohere API: The API used for generating natural language-based code and documentation using large language models.
OpenAI API (optional for future enhancements): Can be integrated for additional NLP functionalities.
Getting Started
Prerequisites
Python 3.x
A Cohere account and API key.
You can sign up for a free trial or use a paid production key from Cohere.
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/ai-code-generation-tool.git
cd ai-code-generation-tool
Install Required Packages:

Install the required dependencies using pip:

bash
Copy code
pip install cohere
Set Up Your API Key:

You need to set your Cohere API key. You can set it as an environment variable:

bash
Copy code
export COHERE_API_KEY="your-cohere-api-key"
Alternatively, you can hard-code the API key in the script, but this is not recommended for security reasons.

Running the Tool
Run the Python Script:

Once you have set up the environment variable or hard-coded the API key, run the tool using the following command:

bash
Copy code
python3 cohere_project.py
Provide a Description:

When prompted, enter a description for the code you want to generate. For example:

"Generate a Python function that prints 'Hello, World!' to the console."

The script will return both the generated Python code and a docstring explaining the code.

Example
Input:
"Generate a Python function that prints 'Hello, World!' to the console."

Output:
python
Copy code
def print_hello_world():
    print("Hello, World!")

print_hello_world()
Generated Documentation:

python
Copy code
"""
Prints 'Hello, World!' to the console.

Usage:
    Call the function `print_hello_world()` to print the message to the console.

Example:
    print_hello_world()  # Output: 'Hello, World!'
"""
Future Enhancements
Support for additional programming languages (e.g., JavaScript, Java).
Advanced customization of docstrings and code style based on user preferences.
Integration with IDEs for seamless code generation and documentation.
License
This project is licensed under the MIT License - see the LICENSE file for details.