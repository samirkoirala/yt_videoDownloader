import tkinter as tk
from tkinter import messagebox
import yt_dlp

def download_video():
    url = url_entry.get()
    try:
        # Validate URL
        if not url.startswith('https://') and not url.startswith('http://'):
            messagebox.showerror("Invalid URL", "Please enter a valid YouTube URL starting with 'https://' or 'http://'")
            return

        messagebox.showinfo("Downloading", "Attempting to download video from URL: " + url)

        ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',
            'format': 'best',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', 'Unknown Title')

        status_label.config(text=f"Video title: {title}")
        messagebox.showinfo("Download Complete", f"Video downloaded successfully")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI setup
root = tk.Tk()
root.title("YouTube Video Downloader")

tk.Label(root, text="YouTube Video URL:").pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=20)

status_label = tk.Label(root, text="")
status_label.pack(pady=10)

root.mainloop()
