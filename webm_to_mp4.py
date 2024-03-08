import os
from moviepy.editor import VideoFileClip

def convert_webm_to_mp4(input_file, output_file):
    # Загрузка видео из .webm файла
    video_clip = VideoFileClip(input_file)
    # Сохранение видео в .mp4 файл
    video_clip.write_videofile(output_file, codec='libx264')
    # Освобождение ресурсов
    video_clip.close()

def main():
    # Получение списка всех файлов в текущей директории
    files = os.listdir('.')
    for file in files:
        # Проверка, является ли файл файлом с расширением .webm
        if file.endswith('.webm'):
            # Создание имени для нового файла с расширением .mp4
            output_file = os.path.splitext(file)[0] + '.mp4'
            # Конвертация .webm в .mp4
            convert_webm_to_mp4(file, output_file)

if __name__ == "__main__":
    main()
