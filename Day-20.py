from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(text, output_file):
    """
    Generates a WordCloud from the given text and saves it as an image file.
    
    Args:
        text (str): The input text for the WordCloud.
        output_file (str): The file path to save the WordCloud image.
    """
    # Generate the WordCloud
    wordcloud = WordCloud(width=800, height=400, background_color="white", colormap="viridis").generate(text)
    
    # Save the WordCloud as an image file
    wordcloud.to_file(output_file)
    
    # Display the WordCloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

# Input text and output file path
text = "data science machine learning artificial intelligence"
output_file = "wordcloud.png"

# Generate and save the WordCloud
generate_wordcloud(text, output_file)

print(f"WordCloud saved as {output_file}")
