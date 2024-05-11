# PDF and YouTube Processor

This project involves a desktop application developed using Tkinter, which allows users to process YouTube videos and PDF files. The application provides functionalities for downloading, transcribing, sentiment analysis, and communication of results via email. Below is a detailed description of each component of the project.

## Components

### Main Application (`main.py`)

- **GUI**: Utilizes Tkinter to provide a user interface where users can choose to process a YouTube video or a PDF file.
- **YouTube Processing**:
  - Users input a YouTube URL, which the application uses to download the video's audio, transcribe it to text, perform sentiment analysis, and optionally email the results.
- **PDF Processing**:
  - Users upload a PDF file, which is converted into images, then to text. The text is analyzed for sentiment and optionally emailed.
- **Email and Cleanup**:
  - After processing, the application can send the results via email and delete temporary files.

### YouTube Audio to Text (`ytAudio2text.py`)

- Downloads audio from a YouTube URL using `pytube`.
- Transcribes audio to text using OpenAI's Whisper model.
- Detects the language of the transcribed text using `langdetect`.

### PDF to Text (`pdf2text.py`)

- Converts PDF files to images using `pdf2image`.
- Extracts text from these images using Tesseract OCR (`pytesseract`).
- Combines extracted text into a single file.

### Text Classification (`classify.py`)

- Analyzes the sentiment of the text using `TextBlob`.
- Classifies text into positive, negative, or neutral categories.
- Stores results in respective files based on their sentiment classification.

### Sending Email (`SendMail.py`)

- Implements SMTP protocol to send an email with attachments using Gmail’s SMTP server.
- Attaches classified text files to the email.

### File Deletion (`DeleteFiles.py`)

- Deletes specified files, cleaning up any temporary or output files created during the process.

## Technology Stack

- **Python**: Main programming language used.
- **Tkinter**: For creating the GUI.
- **Whisper**: For audio transcription.
- **TextBlob**: For sentiment analysis.
- **Tesseract OCR**: For text extraction from images.
- **Pytube**: For downloading YouTube videos.
- **pdf2image**: For converting PDF pages to images.
- **SMTP**: For sending emails.

This application is suitable for tasks like content monitoring, academic research, or enhancing accessibility of multimedia and document content through text and sentiment analysis.
