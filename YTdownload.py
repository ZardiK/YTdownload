import os
from tkinter import Tk, Label, Button, StringVar, Entry, Frame, messagebox
import yt_dlp

def download_youtube_video(url):
    try:
        # Получаем путь к домашней директории текущего пользователя
        home_directory = os.path.expanduser("~")
        # Создаем путь к папке "YouTubeDownloads" в папке загрузок
        download_folder = os.path.join(home_directory, "Downloads", "YouTubeDownloads")
        os.makedirs(download_folder, exist_ok=True)

        ydl_opts = {
            'format': 'best',  # Загружаем лучшее доступное качество
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Путь к файлу
            'noplaylist': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Успех", "Видео успешно загружено!")

    except Exception as e:
        print(f"Ошибка: {e}")
        messagebox.showerror("Ошибка загрузки", str(e))

def create_interface():
    global url_var

    frame = Frame(root, padx=20, pady=20, bg="#2C3E50")
    frame.pack(pady=10)

    title = Label(frame, text="YouTube Video Downloader", font=("Helvetica", 24, "bold"), bg="#2C3E50", fg="#ECF0F1")
    title.grid(row=0, column=0, columnspan=2)

    Label(frame, text="Введите URL:", font=("Helvetica", 14), bg="#2C3E50", fg="#ECF0F1").grid(row=1, column=0)
    url_entry = Entry(frame, textvariable=url_var, width=50, font=("Helvetica", 12), bd=2, relief='groove')
    url_entry.grid(row=1, column=1)

    download_button = Button(frame, text="Скачать", command=lambda: download_youtube_video(url_var.get()), font=("Helvetica", 14),
                             bg="#27AE60", fg="white", relief='flat')
    download_button.grid(row=2, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = Tk()
    root.title("YouTube Video Downloader")
    root.geometry("600x200")

    url_var = StringVar()

    create_interface()
    root.mainloop()
