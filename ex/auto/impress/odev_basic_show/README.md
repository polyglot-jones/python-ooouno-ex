# Impress Basic Slide Show

<p align="center">
    <img src="https://user-images.githubusercontent.com/4193389/198407936-7865b1c2-75b7-4530-8598-a1ce52821752.png" width="448" height="448">
</p>

Demonstrates displaying a slide show using default `algs.odp` file.

A message box is display once the slide show has ended asking if you want to close the document.

This demo uses [OOO Development Tools]

See Also:

- [OOO Development Tools - Part 3: Draw & Impress](https://python-ooo-dev-tools.readthedocs.io/en/latest/odev/part3/index.html)

## Automate

A single parameters can be passed in which is the slide show document to display:

**Example:**

```sh
python ./ex/auto/impress/odev_basic_show/start.py "resources/presentation/algs.ppt"
```

If no parameters are passed then the script is run with the above parameters.

### Cross Platform

From current example folder.

```sh
python -m start
```

### Linux/Mac

```sh
python ./ex/auto/impress/odev_basic_show/start.py
```

### Windows

```ps
python .\ex\auto\impress\odev_basic_show\start.py
```

[OOO Development Tools]: https://python-ooo-dev-tools.readthedocs.io/en/latest/