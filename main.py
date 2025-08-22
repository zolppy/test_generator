import os
from typing import Optional
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import AzureChatOpenAI

# Load environment variables
load_dotenv()

class TestGenerator:
    """
    A class to generate unit tests for Python code using Azure OpenAI's ChatGPT model.
    
    Attributes:
        llm (AzureChatOpenAI): The Azure OpenAI language model instance.
        chain (LLMChain): The language model chain for test generation.
    """
    
    def __init__(self):
        """
        Initializes the TestGenerator with Azure OpenAI configuration.
        Raises an exception if required environment variables are missing.
        """
        # Validate environment variables
        required_env_vars = {
            "AZURE_OPENAI_DEPLOYMENT_NAME": os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            "AZURE_OPENAI_MODEL_NAME": os.getenv("AZURE_OPENAI_MODEL_NAME"),
            "AZURE_OPENAI_API_KEY": os.getenv("AZURE_OPENAI_API_KEY"),
            "AZURE_OPENAI_API_VERSION": os.getenv("AZURE_OPENAI_API_VERSION"),
            "AZURE_OPENAI_ENDPOINT": os.getenv("AZURE_OPENAI_ENDPOINT")
        }
        
        missing_vars = [var for var, val in required_env_vars.items() if not val]
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

        # Initialize LLM
        self.llm = AzureChatOpenAI(
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            model=os.getenv("AZURE_OPENAI_MODEL_NAME", ""),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION", ""),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            temperature=0.3,
            max_retries=3
        )
        
        # Create prompt template
        self.prompt_template = PromptTemplate(
            input_variables=["code_snippet"],
            template="""
            You are an expert in Python unit testing with pytest.

            Analyze the following Python code and generate comprehensive unit tests:
            - Cover success cases, error conditions, and edge cases
            - Use pytest framework with appropriate assertions
            - Include brief comments to explain each test case
            - Return only valid Python code without any additional text

            Code to test:
            {code_snippet}

            Generated tests:
            """
        )
        
        # Initialize LLM chain
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)
    
    def generate_tests(self, code_snippet: str) -> Optional[str]:
        """
        Generates unit tests for the provided code snippet.
        
        Args:
            code_snippet (str): Python code to generate tests for
            
        Returns:
            Optional[str]: Generated test code if successful, None otherwise
        """
        try:
            response = self.chain.run(code_snippet=code_snippet)
            return response.strip()
        except Exception as e:
            print(f"Error generating tests: {str(e)}")
            return None

def main():
    """
    Main function to demonstrate test generation functionality.
    """
    try:
        generator = TestGenerator()
    except ValueError as e:
        print(f"Configuration error: {e}")
        print("Please check your environment variables and try again.")
        return
    
    sample_code = """
    def calculator(a, b, operator):
        if operator == 'addition':
            return a + b
        elif operator == 'subtraction':
            return a - b
        elif operator == 'multiplication':
            return a * b
        elif operator == 'division':
            if b == 0:
                raise ValueError("Division by zero not allowed")
            return a / b
        else:
            raise ValueError("Operation not supported")
    """
    
    print("🧪 Generating unit tests for the provided code...\n")
    
    tests = generator.generate_tests(sample_code)
    if not tests:
        print("Failed to generate tests. Please check your configuration and try again.")
        return
    
    print("✅ Successfully generated tests:\n")
    print(tests)
    
    # Save to file
    try:
        with open("generated_tests.py", "w") as f:
            f.write(tests)
        print(f"\n💾 Tests saved to 'generated_tests.py'")
    except IOError as e:
        print(f"Error saving tests to file: {e}")

if __name__ == "__main__":
    main()