""" Перевод csv файлов из кодировки windows-1251 в MacCyrillic и наоборот. Управление через консоль. """

import os


enc: dict = {"mac": 'MacCyrillic', "windows": 'windows-1251', "utf": 'utf-8', "latin1": "iso-8859-1"}
mac_dir: str = os.path.join(os.getcwd(), 'mac_cyrillic')
win_dir: str = os.path.join(os.getcwd(), 'windows_1251')
files_csv: list[str] = [csv for csv in os.listdir(os.getcwd()) if csv.endswith('.csv')]

def convert_encoding(input_file: str, out_path: str, input_encoding: str, output_encoding: str) -> None:
    """
    Перекодирование стандартной библиотекой.
    :param input_file: файл для смены кодировки
    :param out_path: директория, куда сохранить новый файл
    :param input_encoding: кодировка исходного файла
    :param output_encoding: целевая кодировка
    """
    file_name: str = os.path.basename(input_file).split('.')[0]
    output_file: str = os.path.join(out_path, f"{file_name}_{output_encoding}.csv")

    with open(input_file, 'r', encoding=input_encoding) as infile:
        content = infile.read()
    try:
        with open(output_file, 'w', encoding=output_encoding) as outfile:
            outfile.write(content)
    except Exception as exc:
        os.remove(output_file)
        raise exc

    print(f"Файл успешно конвертирован из [ {input_encoding} ] в [ {output_encoding} ]\n"
          f"и сохранен в каталоге [ {os.path.basename(out_path)} ] -> {os.path.basename(output_file)}\n"
          f"{'-' * 50}\n")


def main():
    command_to_convert = input(f'{"-" * 50}\n'
                               f'Найдены следующие файлы: {files_csv}\n'
                               f'Конвертировать их в другую кодирову?\n'
                               f'Нажмите [Enter] или введите "Нет" '
                               f'\n{"-" * 50}\n')

    if command_to_convert.lower() == 'нет':
        exit(0)

    for file_name in files_csv:
        file_path = os.path.join(os.getcwd(), file_name)
        print(f"{'-' * 50}\n{file_path}")
        try:
            os.makedirs('mac_cyrillic', exist_ok=True)
            convert_encoding(file_path, out_path=mac_dir, input_encoding=enc['windows'], output_encoding=enc['mac'])
        except:
            os.makedirs('windows_1251', exist_ok=True)
            convert_encoding(input_file=file_path, out_path=win_dir, input_encoding=enc['mac'], output_encoding=enc['windows'])

    input('Нажмите любую клавишу чтобы закрыть окно')

if __name__ == "__main__":
    main()

