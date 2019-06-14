export LC_ALL=C.UTF-8
export LANG=C.UTF-8

tesseract --list-langs

ocrmypdf -l chi_tra src.pdf result.pdf
