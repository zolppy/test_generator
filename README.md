# Project: Unit Test Automation with LangChain and Azure ChatGPT

This project demonstrates the automation of unit test creation using Azure's language models (ChatGPT) in combination with the LangChain library. The system analyzes provided Python source code and generates comprehensive unit tests using the pytest framework.

## 📋 Description

The project consists of a unit test generator that:

- Analyzes Python functions provided as input
- Generates comprehensive unit tests using pytest
- Covers success cases, error conditions, and edge cases
- Includes explanatory comments for each test case
- Saves generated tests to a Python file

## 🛠️ Technologies Used

- **Python 3.8+**
- **LangChain**: Framework for applications with language models
- **Azure ChatGPT**: Azure OpenAI language model
- **pytest**: Testing framework for Python
- **python-dotenv**: Environment variables management

## 📁 Project Structure

```
project/
├── main.py                 # Main test generator code
├── generated_tests.py      # Output file with generated tests (created automatically)
├── .env                   # Environment variables file (not included in repository)
├── requirements.txt       # Project dependencies
└── README.md             # This file
```

## ⚙️ Configuration

### Prerequisites

1. Azure account with access to OpenAI service
2. Python 3.8 or higher installed
3. pip (Python package manager)

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd <directory-name>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure environment variables:
   - Create a `.env` file in the project root
   - Add the following variables with your Azure credentials:

```env
AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name
AZURE_OPENAI_MODEL_NAME=your-model-name
AZURE_OPENAI_API_KEY=your-api-key
AZURE_OPENAI_API_VERSION=your-api-version
AZURE_OPENAI_ENDPOINT=your-endpoint
```

## 🚀 How to Use

Run the main script:

```bash
python main.py
```

The script will:

1. Load environment configurations
2. Initialize the Azure language model
3. Generate tests for an example function (calculator)
4. Save tests to the `generated_tests.py` file

### Customization

To generate tests for your own code, modify the `sample_code` variable in the `main.py` file:

```python
sample_code = """
def your_function(param1, param2):
    # Your code here
    return result
"""
```

## 📝 Example Output

For the calculator function provided as an example, the system generates tests like:

```python
import pytest
from your_module import calculator

def test_calculator_addition():
    """Test addition operation"""
    assert calculator(2, 3, 'addition') == 5

def test_calculator_subtraction():
    """Test subtraction operation"""
    assert calculator(5, 3, 'subtraction') == 2

def test_calculator_multiplication():
    """Test multiplication operation"""
    assert calculator(4, 3, 'multiplication') == 12

def test_calculator_division():
    """Test division operation"""
    assert calculator(10, 2, 'division') == 5

def test_calculator_division_by_zero():
    """Test division by zero raises ValueError"""
    with pytest.raises(ValueError, match="Division by zero not allowed"):
        calculator(10, 0, 'division')

def test_calculator_unsupported_operation():
    """Test unsupported operation raises ValueError"""
    with pytest.raises(ValueError, match="Operation not supported"):
        calculator(10, 2, 'modulus')
```

## 🔧 Possible Customizations

1. **Modify the prompt**: Edit the template in `self.prompt_template` to change the style of generated tests
2. **Add more examples**: Include more example functions to test different code patterns
3. **Integrate with CI/CD**: Adapt the code to run automatically in continuous integration pipelines
4. **Support other languages**: Modify the prompt to generate tests for other programming languages

## 🤝 Contribution

Contributions are welcome! Feel free to:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is under the MIT license. See the [LICENSE](LICENSE) file for details.

## 🎯 Learning Objectives

This project enabled the development of the following skills:

- Integration with Azure's language model APIs
- Using the LangChain library for chain operations
- Automation of software development processes
- Code generation through language models
- Configuration and management of environment variables
- Documentation of technical projects
