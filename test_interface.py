from react_langchain_agent.interface.app import process_input, create_interface

def test_process_input():
    print("Testing process_input function...")
    test_input = "What is the length of the word: hello"
    try:
        result, logs = process_input(test_input)
        print("\nTest input:", test_input)
        print("\nAgent response:", result)
        print("\nExecution logs:", logs)
        print("\nprocess_input test passed!")
    except Exception as e:
        print("Error in process_input:", str(e))
        return False
    return True

def test_interface_creation():
    print("\nTesting interface creation...")
    try:
        interface = create_interface()
        print("Interface created successfully!")
        print("Interface configuration:")
        print(f"- Title: {interface.title}")
        print(f"- Number of inputs: {len(interface.input_components)}")
        print(f"- Number of outputs: {len(interface.output_components)}")
        print("\nInterface creation test passed!")
    except Exception as e:
        print("Error creating interface:", str(e))
        return False
    return True

if __name__ == "__main__":
    all_passed = True
    
    # Test process_input
    if not test_process_input():
        all_passed = False
    
    # Test interface creation
    if not test_interface_creation():
        all_passed = False
    
    if all_passed:
        print("\nAll tests passed! The Gradio interface should work correctly.")
        print("You can now run the interface with:")
        print("python -m react_langchain_agent.interface.app")
    else:
        print("\nSome tests failed. Please check the errors above.") 