from setuptools import setup

APP = ['GUI/GuiMain.py']
DATA_FILES = ['icon/icon.icns']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon/icon.icns',
}

setup(
    app=APP,
    name='Demucs-GUI',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
