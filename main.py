import shutil
import os
from utils.config import Config
from src.pdf_png_pdf import PdfPngPdf


paths = Config.PATHS
with os.scandir(path=r'docs\input') as entries:
    for entry in entries:
        if entry.name.endswith('pdf'):
            file = entry.name
            folder = fr'{paths["pics"]}\{entry.name.replace(".", "")}'
            os.mkdir(folder)
            PdfPngPdf.convert_pdf_to_images(fr'{paths["input"]}\{file}', folder)
            shutil.move(fr'{paths["input"]}\{file}', fr'{paths["processed"]}\{file}')
            PdfPngPdf.convert_images_to_pdf(folder, fr'{paths["output"]}\{file}')
            shutil.rmtree(folder, ignore_errors=True)
