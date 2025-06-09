# Credit Card Fraud Detection 
IDs: 314752841, 207851064, 209466721, 20685208 <br />
Names: Michael Livshits, Shon Platok, Rotem Atar, Naveh Gershoni

# Loading the dataset:
Run the notebook it should work as is <br />
If there are problems: exit pycharm and open again, then run the notebook again

# Files & Info
This is a Machine Learning project, which aims to detect (with the highest accuracy) any
fraudulent activity in credit card transaction

1. fraud_detection.ipynb is the Machine Learning project 
2. Emulator is a side project for emulating a payment gateway that handles payment requests <br /> The folder contains: <br /> client.py - this is the program a client opens for sending payment information (Credit Card info) <br /> server.py - this is the payment gateway, it opens a port and accepts requests from clients that open the client.py file the server then processes the incoming request. <br />
The main goal in this emulation is for testing Honey Tokens and showing what they can do. <br />
We will inject some fake credit card information and track any payments that use these tokens thereby exposing malicious actors.  
3. detect_fraud.py - a python script that utilizes the learned model from the project

# detect_fraud.py - Instructions
- Input: a path to a .csv file of transactions
- Output: predictions.csv file of the predicted values for the data
- Example: 'python .\detect_fraud.py <path_to_data>'

### Important - the input data HAS to have the correct feature names, the script won't work otherwise
For valid inputs, check tests/test.csv for a valid example <br />
Additionally you can run the test samples with: <br /> python .\detect_fraud.py tests/test.csv <br />

