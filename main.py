import tkinter as tk
from tkinter import filedialog, messagebox
import ytAudio2text
import pdf2text
import classify
import SendMail
import DeleteFiles
import os

class App:
#GUI for processing yt video and pdf file

    def __init__(self, root):
        #Initialize the main window
        self.root = root
        self.root.title("PDF and YouTube Processor")
        self.create_screen1()

    def create_screen1(self):
        #options to process yt videos or pdf files
        self.clear_frame()

        youtube_button = tk.Button(self.root, text="Process YouTube Video", command=self.youtube_button_click)
        youtube_button.pack(pady=10)

        pdf_button = tk.Button(self.root, text="Upload and Process PDF File", command=self.pdf_button_click)
        pdf_button.pack(pady=10)

    def youtube_button_click(self):
        self.clear_frame()

        youtube_url_label = tk.Label(self.root, text="Enter YouTube URL:")
        youtube_url_label.pack(pady=5)

        self.youtube_url_entry = tk.Entry(self.root, width=50)
        self.youtube_url_entry.pack(pady=5)

        submit_button = tk.Button(self.root, text="Submit", command=self.submit_youtube_url)
        submit_button.pack(pady=10)

    def pdf_button_click(self):
        pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if pdf_path:
            self.process_pdf_file(pdf_path)
            self.create_screen3()

    def submit_youtube_url(self):
        url = self.youtube_url_entry.get()
        self.process_youtube_video(url)
        self.create_screen3()

    def process_youtube_video(self, url):
        try:
            output_filename = ytAudio2text.main(url)
            classify.main(output_filename)
        except Exception as e:
            messagebox.showerror("Processing Error", f"Failed to process YouTube video: {str(e)}")

    def process_pdf_file(self, pdf_path):
        """Process the PDF file, convert to text, and classify the text."""
        try:
            pdf2text.main(pdf_path)
            input_filename = 'combined_text.txt'
            classify.main(input_filename)
        except Exception as e:
            messagebox.showerror("Processing Error", f"Failed to process PDF file: {str(e)}")

    def create_screen3(self):
        #another file or not
        self.clear_frame()

        question_label = tk.Label(self.root, text="Do you want to process another file?")
        question_label.pack(pady=20)

        yes_button = tk.Button(self.root, text="Yes", command=self.create_screen1)
        yes_button.pack(side=tk.LEFT, padx=20)

        no_button = tk.Button(self.root, text="No", command=self.create_screen4)
        no_button.pack(side=tk.RIGHT, padx=20)

    def create_screen4(self):
        #enter receiver's mail
        self.clear_frame()

        email_label = tk.Label(self.root, text="Enter your email address:")
        email_label.pack(pady=5)

        self.email_entry = tk.Entry(self.root, width=50)
        self.email_entry.pack(pady=5)

        done_button = tk.Button(self.root, text="Done", command=self.send_email)
        done_button.pack(pady=10)

    def send_email(self):
        email = self.email_entry.get()
        SendMail.send_email(email)

        # Delete files
        files = ['negative.txt', 'positive.txt', 'neutral.txt']
        folder = 'classified_text'
        full_file_paths = [os.path.join(folder, file) for file in files]
        DeleteFiles.delete_files(full_file_paths)

        messagebox.showinfo("Success", "Files sent successfully!")
        self.root.destroy()

    def clear_frame(self):
        """Clear the frame of all widgets."""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
