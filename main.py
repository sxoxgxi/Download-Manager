import os
import shutil


PARENT_DIR = r'C:\Users\janak\Downloads'
AUDIO_DIR = r'C:\Users\janak\Downloads\Audios'
DOCUMENT_DIR = r'C:\Users\janak\Downloads\Documents'
DATAFILE_DIR = r'C:\Users\janak\Downloads\Datafiles'
VIDEO_DIR = r'C:\Users\janak\Downloads\Videos'
IMAGE_DIR = r'C:\Users\janak\Downloads\Images'
EXECUTABLE_DIR = r'C:\Users\janak\Downloads\Executables'
OTHER_DIR = r'C:\Users\janak\Downloads\Others'


IMAGES_FILES = [
    '.jpg', '.jpeg', '.jfif', '.pjpeg', '.pjp', '.png',
    '.gif', '.webp', '.svg', '.apng', '.avif'
]

VIDEOS_FILES = [
    '.webm', '.mts', '.m2ts', '.ts', '.mov',
    '.mp4', '.m4p', '.m4v', '.mxf'
]

AUDIO_FILE = [
    '.3ga', '.aac', '.ac3', '.aif', '.aiff',
    '.alac', '.amr', '.ape', '.au', '.dss',
    '.flac', '.flv', '.m4a', '.m4b', '.m4p',
    '.mp3', '.mpga', '.ogg', '.oga', '.mogg',
    '.opus', '.qcp', '.tta', '.voc', '.wav',
    '.wma', '.wv'
]

DOCUMENTS_FILES = [
    '.doc', '.docx', '.log', '.msg', '.odt',
    '.pages', '.rtf', '.tex', '.txt', '.wpd',
    '.wps', '.indo', '.pct', '.pdf'
]

DATA_FILES = [
    '.csv', '.dat', '.ged', '.key', '.keychain',
    '.ppt', '.pptx', '.sdf', '.tar', '.tax2016',
    '.tax2020', '.tax2021', '.vcf', '.xml', '.zip'
]

EXECUTABLE_FILES = [
    '.bat', '.bin', '.cmd', '.com', '.cpl', '.ex_', '.exe',
    '.gadget', '.inf1', '.ins', '.inx', '.isu', '.job',
    '.jse', '.lnk', '.msc', '.msi', '.msp', '.mst', '.paf',
    '.pif', '.ps1', '.reg', '.rgs', '.scr', '.sct',
    '.shb', '.shs', '.ws', '.wsf', '.wsh', '.py'
]


def main():
    print("Trying to manage the files...")
    os.chdir(PARENT_DIR)

    dirs = [
        'Audios', 'Images', 'Documents', 'Videos', 'Datafiles', 'Others', 'Executables'
    ]

    for file in os.listdir():
        audio = os.path.splitext(file)[1] in AUDIO_FILE
        video = os.path.splitext(file)[1] in VIDEOS_FILES
        images = os.path.splitext(file)[1] in IMAGES_FILES
        data = os.path.splitext(file)[1] in DATA_FILES
        documents = os.path.splitext(file)[1] in DOCUMENTS_FILES
        executables = os.path.splitext(file)[1] in EXECUTABLE_FILES
        if file not in dirs:
            if data:
                shutil.move(file, DATAFILE_DIR)
            elif documents:
                shutil.move(file, DOCUMENT_DIR)
            elif audio:
                shutil.move(file, AUDIO_DIR)
            elif video:
                shutil.move(file, VIDEO_DIR)
            elif images:
                shutil.move(file, IMAGE_DIR)
            elif executables:
                shutil.move(file, EXECUTABLE_DIR)
            else:
                shutil.move(file, OTHER_DIR)

    print(f"Done managing the downloads area!\n\"{os.getcwd()}\"")


if __name__ == '__main__':
    main()
