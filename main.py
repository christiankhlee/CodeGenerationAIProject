import openai
import os
import time

# Set the OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_code(description):
    try:
        response = openai.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            prompt=description,
            max_tokens=150,
            n=1,
            temperature=0.7
        )
        return response['choices'][0]['text'].strip()
    except openai.error.RateLimitError:
        print("Rate limit exceeded. Retrying in 5 seconds...")
        time.sleep(5)  # Wait before retrying
        return generate_code(description)  # Retry the request

def generate_documentation(code):
    try:
        doc_prompt = f"Generate a docstring for the following Python code:\n{code}"
        response = openai.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            prompt=doc_prompt,
            max_tokens=150,
            n=1,
            temperature=0.7
        )
        return response['choices'][0]['text'].strip()
    except openai.error.RateLimitError:
        print("Rate limit exceeded. Retrying in 5 seconds...")
        time.sleep(5)  # Wait before retrying
        return generate_documentation(code)  # Retry the request

def main():
    description = input("Enter a description for the code you want to generate: ")
    
    # Generate code based on the description
    generated_code = generate_code(description)
    
    # Generate documentation for the generated code
    generated_docs = generate_documentation(generated_code)
    
    print("\nGenerated Code:\n")
    print(generated_code)
    
    print("\nGenerated Documentation:\n")
    print(generated_docs)

if __name__ == "__main__":
    main()
