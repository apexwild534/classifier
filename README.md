# PDF and YouTube Processor

This application processes YouTube videos and PDF files to classify text into positive, negative, or neutral sentiments using [TextBlob](https://textblob.readthedocs.io/en/dev/). The results can be reviewed and sent via email as needed.

## Getting Started

Follow these steps to set up and run the classifier:

1. **Clone the Repository**
   - Clone or download this repository to your local machine.

2. **Install Dependencies**
   - If this is your first time using TextBlob, install it along with its necessary corpora:
     ```bash
     pip install -U textblob
     python -m textblob.download_corpora
     ```

   - Check for tkinter package if not installed install it for your os

3. **Install Additional Packages**
   - Install other required packages as specified in [requirements.txt](requirements.txt). Note: Some packages may not be compatible with Python 3.12. It's recommended to use Python versions 3.8 to 3.11 or Python3(Linux), a venv is recommended.
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the Application**
   - Run the [main.py](main.py) file using a Python3 interpreter through an IDE like PyCharm, Visual Studio Code, or any other preferred IDE.

5. **Access Resources**
   - For YouTube links, refer to [Trial Links](links.txt).
   - For testing with a PDF, use the provided [Newspaper](toi.pdf) file.

6. **Explore**
   - Enjoy using the **CLASSIFIER** to process and analyze content.

For a detailed explanation of each component and the technology stack of the application, refer to [Explanation.md](Explanation.md).
