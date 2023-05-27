import tkinter as tk
import webbrowser
from PIL import ImageTk, Image

# Function to open the YouTube video
def show_video():
    youtube_url = "https://www.youtube.com/watch?v=eOrNdBpGMv8"  # Replace YOUR_VIDEO_ID with the actual YouTube video ID
    webbrowser.open(youtube_url)

# Create the main window
window = tk.Tk()

# Set the window title
window.title("Graphics Demo")

# Create a label with the question and configure its font size
question_label = tk.Label(window, text="What's my favorite Movie?", font=("Arial", 16))
question_label.configure(fg="red")
question_label.pack()

# Load the image
image_path = "youtube_logo.png"  # Replace with the path to your image file
image = Image.open(image_path)
resized_image = image.resize((200, 200))  # Adjust the size of the image if needed
photo = ImageTk.PhotoImage(resized_image)

# Create a button to show the image
image_button = tk.Button(window, image=photo, command=show_video)
image_button.pack()

# Create a button to open YouTube
youtube_button = tk.Button(window, text="Click to find out!", command=show_video)
youtube_button.configure(fg="red")
youtube_button.pack()

# Run the main event loop
window.mainloop()
