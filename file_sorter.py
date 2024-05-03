from pathlib import Path
from shutil import copyfile
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import logging


output_folder = Path('Dict')
quantity_threads = 5
# def read_folder(path:Path) -> None:
#     for element in path.iterdir():
#         if element.is_dir():
#             read_folder(element)
#         else:
#             copy_file(element)


def read_folder(path: Path) -> None:

    files = [element for element in path.iterdir() if element.is_file()]
    with ThreadPoolExecutor() as executor:
        executor.map(copy_file, files)


def copy_file(file:Path) -> None:
    extension = file.suffix
    new_path = output_folder / extension[1:]
    new_path.mkdir(parents=True, exist_ok=True)
    copyfile(file, new_path/file.name)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(thread_name)s:%(message)s')
    read_folder(Path('pictures'))

    # threads = []
    # for element in output_folder.iterdir():
    #     th = Thread(target=copy_file, args=(element,))
    #     th.start()
    #     threads.append(th)
    #
    # [th.join() for th in threads]

    print(f"Можна видалять {Path('pictures')}")




