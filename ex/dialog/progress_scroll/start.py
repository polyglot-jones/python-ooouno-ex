#
# on wayland (some versions of Linux)
# may get error:
#    (soffice:67106): Gdk-WARNING **: 02:35:12.168: XSetErrorHandler() called with a GDK error trap pushed. Don't do that.
# This seems to be a Wayland/Java compatibility issues.
# see: http://www.babelsoft.net/forum/viewtopic.php?t=24545
from __future__ import annotations
import uno
from ooodev.utils.lo import Lo
from ooodev.calc import CalcDoc
from progress import Progress


def main() -> int:
    with Lo.Loader(Lo.ConnectSocket(), opt=Lo.Options(verbose=True)):
        doc = CalcDoc.create_doc(visible=True)

        Lo.delay(300)
        doc.zoom_value(100)
        progress = Progress(doc)
        progress.show()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
