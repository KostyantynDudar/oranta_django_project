import os

# Папка проекта
base_dir = "/home/oranta_django_project"
# Итоговый текстовый файл
output_text_file = os.path.join(base_dir, "collected_texts.txt")

# Расширения файлов, которые нужно включить
allowed_extensions = {".py", ".html", ".js", ".css"}
# Исключить определённые файлы и папки
exclude_files = {"manage.py", "README.md"}
exclude_dirs = {"node_modules", "__pycache__", "staticfiles", "media", "build", "venv", "migrations", "static", "oranta_env"}
# Максимальный размер файла (в байтах) — 1 МБ
max_file_size = 1 * 1024 * 1024  # 1 МБ

# Функция для извлечения текстов из файлов
def extract_texts(source_dir, output_file):
    with open(output_file, "w", encoding="utf-8") as output:  # Перезаписываем файл при каждом запуске
        for root, dirs, files in os.walk(source_dir):
            # Исключаем нежелательные директории
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file in files:
                # Проверяем расширение и исключаем ненужные файлы
                if any(file.endswith(ext) for ext in allowed_extensions) and file not in exclude_files:
                    # Полный путь к файлу
                    file_path = os.path.join(root, file)
                    
                    try:
                        # Проверяем размер файла
                        if os.path.getsize(file_path) > max_file_size:
                            print(f"Пропущен файл (слишком большой): {file_path}")
                            continue

                        # Читаем содержимое файла
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()

                        # Записываем в итоговый файл
                        output.write(f"--- FILE: {file_path} ---\n")
                        output.write(content)
                        output.write("\n\n")  # Разделение между файлами
                        print(f"Обработан файл: {file_path}")
                    except Exception as e:
                        # Обработка ошибок чтения файлов
                        output.write(f"--- FILE: {file_path} ---\n")
                        output.write(f"Ошибка чтения файла: {e}\n\n")
                        print(f"Ошибка чтения файла {file_path}: {e}")

# Основной процесс
def main():
    # Удаляем старый итоговый файл, если он существует
    if os.path.exists(output_text_file):
        os.remove(output_text_file)

    # Извлекаем тексты из текущей папки
    extract_texts(base_dir, output_text_file)

    print(f"Тексты всех файлов сохранены в {output_text_file}")

if __name__ == "__main__":
    main()
