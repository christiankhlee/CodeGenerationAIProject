import cohere
import os
import time

# Set your Cohere API key (ensure the key is either set in an environment variable or replace with the actual key)
cohere_api_key = os.getenv('COHERE_API_KEY')  # Or replace with your actual API key directly

# Initialize Cohere client with your API key
cohere_client = cohere.Client(cohere_api_key)

def generate_code(description):
    try:
        # Generate code using Cohere's API
        response = cohere_client.generate(
            model='command-xlarge',  # Use a valid model like 'command-xlarge'
            prompt=description,
            max_tokens=150,
            temperature=0.7
        )
        return response.generations[0].text.strip()
    except Exception as e:
        print(f"Error generating code: {e}")
        return None

def generate_documentation(code):
    try:
        # Generate documentation (docstring) for the generated code using Cohere's API
        doc_prompt = f"Generate a docstring for the following Python code:\n{code}"
        response = cohere_client.generate(
            model='command-xlarge',  # Use a valid model like 'command-xlarge'
            prompt=doc_prompt,
            max_tokens=150,
            temperature=0.7
        )
        return response.generations[0].text.strip()
    except Exception as e:
        print(f"Error generating documentation: {e}")
        return None

def main():
    description = input("Enter a description for the code you want to generate: ")
    
    # Generate code based on the description
    generated_code = generate_code(description)
    if generated_code:
        print("\nGenerated Code:\n")
        print(generated_code)
    
        # Generate documentation for the generated code
        generated_docs = generate_documentation(generated_code)
        if generated_docs:
            print("\nGenerated Documentation:\n")
            print(generated_docs)
        else:
            print("Error generating documentation.")
    else:
        print("Error generating code.")

if __name__ == "__main__":
    main()
