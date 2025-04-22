#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sample Python script with comments for testing pycommentcleaner.

This file contains various types of comments in different contexts
to demonstrate how pycommentcleaner handles them.
"""

import os  # Import the os module
import sys  # Import the sys module
from typing import List, Dict, Any  # Import type hints


# Define a constant
MAX_VALUE = 100  # Maximum value allowed


class SampleClass:
    """A sample class with methods and comments.
    
    # This comment inside a docstring should not be removed
    """
    
    def __init__(self, name: str):
        # Initialize the object
        self.name = name  # Set the name attribute
        
    def greet(self) -> str:
        """Return a greeting message.
        
        # This is another comment in a docstring
        """
        # Create the greeting
        return f"Hello, {self.name}!"  # Return the formatted string


def process_data(data: List[int]) -> Dict[str, Any]:
    """Process a list of integers and return statistics.
    
    Args:
        data: A list of integers to process
        
    Returns:
        A dictionary with statistics
    """
    # Initialize result dictionary
    result = {}  # This will store our results
    
    # Calculate statistics
    result["sum"] = sum(data)  # Calculate sum
    result["avg"] = sum(data) / len(data) if data else 0  # Calculate average
    result["max"] = max(data) if data else None  # Find maximum value
    
    # String with hash symbol
    example_string = "This # is not a comment"
    
    '''
    This is a multi-line string
    # This comment should not be removed
    because it's inside a string
    '''
    
    # Return the result
    return result


if __name__ == "__main__":
    # This is the main entry point
    
    # Create a sample object
    sample = SampleClass("World")  # Create with name "World"
    
    # Print a greeting
    print(sample.greet())  # This will print "Hello, World!"
    
    # Process some data
    data = [1, 2, 3, 4, 5]  # Sample data
    result = process_data(data)  # Process the data
    
    # Print the results
    print(f"Sum: {result['sum']}")  # Print sum
    print(f"Average: {result['avg']}")  # Print average
    print(f"Maximum: {result['max']}")  # Print maximum
    
    # Exit the program
    sys.exit(0)  # Exit with success code