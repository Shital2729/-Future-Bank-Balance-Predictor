# check_file.py
print("--- Checking model.pkl ---")
try:
    with open('model.pkl', 'rb') as f:
        # Read the first 20 bytes of the file
        content = f.read(20)
        print("The first 20 bytes of the file are:")
        print(content)

        # Check if the file starts with the text of a notebook
        if content.startswith(b'{"cells":'):
            print("\nRESULT: This is a Jupyter Notebook file, not a model file. This is the problem.")
        else:
            print("\nRESULT: This appears to be the correct binary file.")

except FileNotFoundError:
    print("RESULT: The file 'model.pkl' was not found in this directory.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")