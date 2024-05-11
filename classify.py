from textblob import TextBlob
import os

def classify_segment(segment):
#classify a text segment as positive, negative, or neutral based on sentiment polarity
    analysis = TextBlob(segment)
    polarity = analysis.sentiment.polarity

    if polarity > 0.1:
        return 'positive'
    elif polarity < -0.1:
        return 'negative'
    else:
        return 'neutral'

def write_to_file(filename, segments):
    with open(filename, 'a') as file:
        for segment in segments:
            file.write(segment + "\n\n")

def main(input_filename, output_folder='classified_text'):
    #Read text from a file, classify it by sentiment, and save the results in separate files.
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(input_filename, 'r') as file:
        content = file.read()

    segments = content.split('\n\n')

    positive_segments = []
    negative_segments = []
    neutral_segments = []

    for segment in segments:
        category = classify_segment(segment)
        if category == 'positive':
            positive_segments.append(segment)
        elif category == 'negative':
            negative_segments.append(segment)
        else:
            neutral_segments.append(segment)

    positive_file = os.path.join(output_folder, 'positive.txt')
    negative_file = os.path.join(output_folder, 'negative.txt')
    neutral_file = os.path.join(output_folder, 'neutral.txt')

    write_to_file(positive_file, positive_segments)
    write_to_file(negative_file, negative_segments)
    write_to_file(neutral_file, neutral_segments)

    return positive_file, negative_file, neutral_file

# if __name__ == "__main__":
#     input_file = input("Enter the path to the text file: ")
#     main(input_file)
