"""
Example script demonstrating how to use the pycommentcleaner package.
"""

import logging
import os
import sys
from pathlib import Path

# Add the parent directory to sys.path to allow importing the package
# This is only needed for this example script
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pycommentcleaner import clean_code, clean_file


def example_clean_code():
    """Example of using the clean_code function."""
    # Sample Python code with comments
    code = """
# This is a comment at the beginning of the file
def hello():
    # This is a function that prints a greeting
    print("Hello, world!")  # This prints a greeting
    
    string_with_hash = "This # is not a comment"
    '''This is a docstring
    # This is not a comment because it's in a docstring
    '''
"""
    
    # Clean the code
    cleaned_code = clean_code(code)
    
    # Print the original and cleaned code
    print("Original code:")
    print("-" * 40)
    print(code)
    print("-" * 40)
    print("\nCleaned code:")
    print("-" * 40)
    print(cleaned_code)
    print("-" * 40)


def example_clean_file():
    """Example of using the clean_file function."""
    # Create a temporary file with sample code
    temp_file = Path('example_script.py')
    
    # Sample Python code with comments
    code = """
# This is a comment at the beginning of the file
def hello():
    # This is a function that prints a greeting
    print("Hello, world!")  # This prints a greeting
    
    string_with_hash = "This # is not a comment"
    '''This is a docstring
    # This is not a comment because it's in a docstring
    '''
"""
    
    # Write the code to the file
    with open(temp_file, 'w') as f:
        f.write(code)
    
    print(f"Created temporary file: {temp_file}")
    
    # Clean the file
    success, message = clean_file(temp_file)
    
    # Print the result
    if success:
        print(f"Success: {message}")
        
        # Read and print the cleaned file
        cleaned_file = Path('example_script_cleaned.py')
        with open(cleaned_file, 'r') as f:
            cleaned_code = f.read()
        
        print(f"\nContent of {cleaned_file}:")
        print("-" * 40)
        print(cleaned_code)
        print("-" * 40)
    else:
        print(f"Error: {message}")
    
    # Clean up the temporary files
    if temp_file.exists():
        temp_file.unlink()
    
    cleaned_file = Path('example_script_cleaned.py')
    if cleaned_file.exists():
        cleaned_file.unlink()


def main():
    """Run the examples."""
    # Configure logging
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    
    # Run the examples
    print("=" * 40)
    print("Example 1: Using clean_code")
    print("=" * 40)
    example_clean_code()
    
    print("\n" + "=" * 40)
    print("Example 2: Using clean_file")
    print("=" * 40)
    example_clean_file()


if __name__ == "__main__":
    main()