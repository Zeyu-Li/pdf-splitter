# PDF Splitter

A Python script that splits pdf files or get the Windows executable [here](https://github.com/Zeyu-Li/pdf_merger/releases/tag/Version-1)



## Usage

### Windows

For Windows users you can download the latest release [here](https://github.com/Zeyu-Li/pdf_merger/releases/tag/Version-1) or go to [github.com/Zeyu-Li/pdf_merger/releases/tag/Version-1](https://github.com/Zeyu-Li/pdf_merger/releases/tag/Version-1) and click download

Once you unzip you can go in and input your pdf files in the input and click on `split.exe` 

\*Note for the executable you do not need any dependencies as it is already included, in fact, you do **not even need python to run**

### Non Windows

To use either run it with

```bash
python3 split.py 3 5 7
```

\*Numbers at the end that indicate where the breaks occur

Or

```bash
python3 split.py
```

And it will then prompt you for the numbers where the break occur



## Requires

* [PyPDF2](https://pypi.org/project/PyPDF2/) (If you are not running the executable, otherwise no dependencies)



## Licence

MIT
