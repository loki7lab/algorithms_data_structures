'''
Basic Debugging Controls:
F5: Start/Continue debugging
F10: Step Over (execute current line and pause at next line)
F11: Step Into (go into function calls)
Shift+F11: Step Out (exit current function)
F9: Toggle breakpoint (click on line number to add/remove breakpoint)
Shift+F5: Stop debugging
'''
#****************************************************************************
'''
Try this debugging exercise:
Set a breakpoint at def main():
Press F5 to start debugging
Use F10 to step through the main function
When you reach process_data(numbers), use F11 to step into it
Use F10 to step through the loop
Use Shift+F11 to step out of the function
Continue with F10 until the end
'''
from typing import List, Tuple
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def calculate_sum(numbers: List[int]) -> int:
    """
    Calculate the sum of numbers in a list.
    
    Args:
        numbers: List of integers to sum
        
    Returns:
        int: Sum of all numbers
    """
    try:
        return sum(numbers)
    except TypeError as e:
        logger.error(f"Error calculating sum: {e}")
        raise

def process_data(data: List[int]) -> List[int]:
    """
    Process data by doubling each number.
    
    Args:
        data: List of integers to process
        
    Returns:
        List[int]: Processed data with each number doubled
    """
    try:
        return [item * 2 for item in data]  # More efficient list comprehension
    except TypeError as e:
        logger.error(f"Error processing data: {e}")
        raise

def analyze_data(numbers: List[int]) -> Tuple[List[int], int]:
    """
    Analyze data by processing it and calculating sum.
    
    Args:
        numbers: List of integers to analyze
        
    Returns:
        Tuple containing:
        - List of processed numbers
        - Sum of processed numbers
    """
    try:
        doubled = process_data(numbers)
        total = calculate_sum(doubled)
        return doubled, total
    except Exception as e:
        logger.error(f"Error analyzing data: {e}")
        raise

def complex_loop_example(numbers: List[int] = None) -> List[int]:
    """
    Demonstrate complex loop with break and continue.
    
    Args:
        numbers: Optional list of numbers to process
        
    Returns:
        List[int]: Processed numbers
    """
    if numbers is None:
        numbers = [1, 2, 3, 4, 5]
    
    result = []
    try:
        for i, current in enumerate(numbers):
            # Skip even numbers
            if current % 2 == 0:
                continue
                
            # Process number
            processed = current * 2
            result.append(processed)
            
            # Break if we've processed enough numbers
            if len(result) >= 3:
                break
                
    except Exception as e:
        logger.error(f"Error in complex loop: {e}")
        raise
        
    return result

def main() -> None:
    """
    Main function demonstrating the usage of all functions.
    """
    try:
        # Test data
        numbers = [1, 2, 3, 4, 5]
        
        # Process data
        doubled, total = analyze_data(numbers)
        
        # Run complex loop example
        result = complex_loop_example(numbers)
        
        # Log results
        logger.info(f"Original numbers: {numbers}")
        logger.info(f"Doubled numbers: {doubled}")
        logger.info(f"Sum of doubled numbers: {total}")
        logger.info(f"Complex loop result: {result}")
        
    except Exception as e:
        logger.error(f"Error in main: {e}")
        raise

if __name__ == "__main__":
    main() 


