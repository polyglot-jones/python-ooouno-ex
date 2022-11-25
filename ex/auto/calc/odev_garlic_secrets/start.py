#!/usr/bin/env python
# coding: utf-8
#
# on wayland (some versions of Linux)
# may get error:
#    (soffice:67106): Gdk-WARNING **: 02:35:12.168: XSetErrorHandler() called with a GDK error trap pushed. Don't do that.
# This seems to be a Wayland/Java compatability issues.
# see: http://www.babelsoft.net/forum/viewtopic.php?t=24545

import sys
import argparse

from ooodev.utils.file_io import FileIO
from garlic_secrets import GarlicSecrets


def args_add(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-o",
        "--out",
        help="Optional file path of output file",
        action="store",
        dest="out_file",
        default="",
    )


def main() -> int:
    # create parser to read terminal input
    parser = argparse.ArgumentParser(description="main")

    # add args to parser
    args_add(parser=parser)

    # if len(sys.argv) <= 1:
    #     parser.print_help()
    #     return 0

    # read the current command line args
    args = parser.parse_args()

    fnm = "resources/data/produceSales.xlsx"
    if not FileIO.is_exist_file(fnm):
        fnm = "../../../../resources/data/produceSales.xlsx"

    gs = GarlicSecrets(fnm=fnm, out_fnm=args.out_file)
    gs.main()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
