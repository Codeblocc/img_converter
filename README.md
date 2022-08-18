# .JPG to .PNG image converter, made with Python.

This application converts a .JPG file to a .PNG file.

## Modules

Make sure you have the following module installed on your machine:
``pip install Pillow``

Import the following modules and start the process.
``import Sys``
``import Sys``
``from PIL``
``import Image``

Grab the first and second argument using the ``sys.argv[1]`` and ``sys.argv[2]``.
Make sure the sys.argv are command line arguments. Ran them in poweshell instead of Python terminal.

## Code adjustments

Instead of the following code:
``img = Image.open(f'{image_folder}{file}')``, ran the following the code.

``img = Image.open(os.path.join(image_folder, file))``

The first line of code gave me the following error - 

``Traceback (most recent call last):
  File "C:\Users\abhishek.dhar\Desktop\Py\ud py\img_converter\jpg_png_converter.py", line 15, in <module>
  File "C:\Users\abhishek.dhar\AppData\Local\Programs\Python\Python310\lib\site-packages\PIL\Image.py", line 3068, in open
    fp = builtins.open(filename, "rb")
FileNotFoundError: [Errno 2] No such file or directory: '.\\imagesheisenberg2.jpg'``

This was later fixed by referring to [StackOverflow 37261495](https://stackoverflow.com/questions/37261495/fp-builtins-openfilename-rb-error).


### Note

The objective is to save the newly converted files to the New folder, however that's not working as of now. Will update once I have the workaround.
