import tkinter as tk
from tkinter import ttk, messagebox
from pytube import YouTube, Playlist

class YouTubeDownloaderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("YouTube Downloader")
        self.geometry("650x650")
        self.configure(bg="#080100")
        
        self.style = ttk.Style(self)
        self.style.configure("TLabel", background="#080100", foreground="#14f50c", font=("Helvetica", 12, "bold"))
        self.style.configure("TButton", background="#4CAF50", foreground="black", font=("Helvetica", 12, "bold"), padding=10, borderwidth=1, relief="raised")
        self.style.map("TButton", background=[("active", "#45a049")])  # Change background color on hover
        self.style.configure("TEntry", padding=5)
        
        self.create_widgets()
    
    def create_widgets(self):
        # youTube Video Downloader Section this is where out box is made or where we set customization of fonts,bg,fg
        ttk.Label(self, text="YouTube Video Downloader", font=("Helvetica", 16, "bold")).pack(pady=10)
        
        self.video_link_label = ttk.Label(self, text="Video Link:")
        self.video_link_label.pack(pady=5)
        
        self.video_link_entry = ttk.Entry(self, width=50)
        self.video_link_entry.pack(pady=5)
        
        self.quality_label = ttk.Label(self, text="Resolution (360, 720):")
        self.quality_label.pack(pady=5)
        
        self.quality_entry = ttk.Entry(self, width=10)
        self.quality_entry.pack(pady=5)
        
        self.download_video_button = ttk.Button(self, text="Download Video", command=self.download_video)
        self.download_video_button.pack(pady=10)
        
        # this is our logical code like how our code will interact with user
        ttk.Label(self, text="YouTube Playlist Downloader", font=("Helvetica", 16, "bold")).pack(pady=10)
        
        self.playlist_link_label = ttk.Label(self, text="Playlist Link:")
        self.playlist_link_label.pack(pady=5)
        
        self.playlist_link_entry = ttk.Entry(self, width=50)
        self.playlist_link_entry.pack(pady=5)
        
        self.playlist_quality_label = ttk.Label(self, text="Resolution (360):")
        self.playlist_quality_label.pack(pady=5)
        
        self.playlist_quality_entry = ttk.Entry(self, width=10)
        self.playlist_quality_entry.pack(pady=5)
        
        self.download_playlist_button = ttk.Button(self, text="Download Playlist", command=self.download_playlist)
        self.download_playlist_button.pack(pady=10)
     #now this is our logic
    def download_video(self):
        video_link = self.video_link_entry.get()
        quality = self.quality_entry.get()
        
        if not video_link or not quality:
            messagebox.showerror("Error", "Please enter both video link and quality.")
            return
        
        try:
            yt = YouTube(video_link)
            if quality == '360':
                stream = yt.streams.filter(file_extension='mp4', resolution="360p").first()
            elif quality == '720':
                stream = yt.streams.filter(file_extension='mp4', resolution="720p").first()
            else:
                messagebox.showerror("Error", "Invalid quality. Please enter 360 or 720.")
                return
            
            if stream:
                stream.download()
                messagebox.showinfo("Success", f"Your download is starting in {quality}p and will be stored in the current directory.")
            else:
                messagebox.showerror("Error", f"No stream found for {quality}p.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def download_playlist(self):
        playlist_link = self.playlist_link_entry.get()
        quality = self.playlist_quality_entry.get()
        
        if not playlist_link or not quality:
            messagebox.showerror("Error", "Please enter both playlist link and quality.")
            return
        
        try:
            playlist = Playlist(playlist_link)
            if quality == '360':
                for video in playlist.videos:
                    stream = video.streams.filter(resolution="360p").first()
                    if stream:
                        stream.download()
                messagebox.showinfo("Success", "Your playlist is being downloaded in 360p, please be patient.")
            else:
                messagebox.showerror("Error", "Invalid quality. Please enter 360.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = YouTubeDownloaderApp()
    app.mainloop()
