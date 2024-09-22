## Simple image file renamer

    Takes file's os.path.getmtime and makes filename prefix in following format:
    'IMG_YYYYMMDD_HHMMSS_OLD_FILE_NAME'

### 1. Uses given extension or .jpg by default.
### 2. Checks for image corruption with Pillow lib.
### 3. Recursively walks through subdirectories starting from current directory where util is executed.
### 4. Doesn't affect files which already been renamed.

    Examples:
    >: python.exe x:\projects\renamer\renamer.py
    >: python.exe x:\projects\renamer\renamer.py .png

#### To make executable use pyinstaller lib 

    Windows:
    >: pyinstaller --noconsole --onefile .\renamer.py

    Then use renamer:
    >: x:\projects\renamer\renamer.exe
    >: x:\projects\renamer\renamer.exe .png