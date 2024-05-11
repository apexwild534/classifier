from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import os

def convert_pdf_to_images(pdf_path, output_folder='converted_images'):
    images = convert_from_path(pdf_path)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, image in enumerate(images):
        image.save(f"{output_folder}/image_{i}.jpg", "JPEG")

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def convert_image_to_text(image_path, output_folder='converted_text'):
    text = extract_text_from_image(image_path)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    text_file_path = os.path.join(output_folder, os.path.basename(image_path).replace('.', '_') + '.txt')
    with open(text_file_path, 'w') as f:
        f.write(text)
    return text_file_path

def combine_text_files(file_paths, combined_file_path='combined_text.txt'):
    with open(combined_file_path, 'w') as outfile:
        for file_path in file_paths:
            with open(file_path, 'r') as infile:
                outfile.write(infile.read())
                outfile.write("\n\n")

def main(pdf_path, images_folder='converted_images', text_folder='converted_text'):
    convert_pdf_to_images(pdf_path, images_folder)

    text_file_paths = []
    if os.path.exists(images_folder):
        for image_file in os.listdir(images_folder):
            if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(images_folder, image_file)
                text_file_path = convert_image_to_text(image_path, text_folder)
                text_file_paths.append(text_file_path)

    combined_file_path = 'combined_text.txt'
    combine_text_files(text_file_paths, combined_file_path)
    return combined_file_path

# if __name__ == "__main__":
#     pdf_path_input = input("Enter the path to the PDF file: ")
#     main(pdf_path_input)
