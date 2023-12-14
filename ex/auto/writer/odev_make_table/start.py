from __future__ import annotations
import csv
from pathlib import Path
from typing import List

from ooodev.dialog.msgbox import (
    MsgBox,
    MessageBoxType,
    MessageBoxButtonsEnum,
    MessageBoxResultsEnum,
)
from ooodev.utils.lo import Lo
from ooodev.office.write import Write
from ooodev.utils.gui import GUI
from ooodev.utils.date_time_util import DateUtil
from ooodev.format.writer.style.para import Para as ParaStyle


def read_table(fnm: Path) -> List[list]:
    # get a 2D Table with the the first row containing column names.
    results = []
    with open(fnm, "r", newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="\t")
        line_count = 0
        for row in csv_reader:
            # each row is a list of values
            if line_count in (0, 1, 2, 4):  # skip non-csv lines
                line_count += 1
                continue
            # first row will be column names
            results.append(row)
            line_count += 1
    return results


def main() -> int:
    fnm = Path(__file__).parent / "data" / "bondMovies.txt"  # source csv file

    tbl_data = read_table(fnm)

    delay = 2_000  # delay so users can see changes.

    loader = Lo.load_office(Lo.ConnectSocket())

    try:
        doc = Write.create_doc(loader=loader)
        GUI.set_visible(visible=True, doc=doc)

        cursor = Write.get_cursor(doc)

        Write.append_para(cursor, "Table of Bond Movies", styles=[ParaStyle().h1])

        Write.append_para(cursor, 'The following table comes form "bondMovies.txt"\n')

        # Lock display updating for faster writing of table into document.
        with Lo.ControllerLock():
            Write.add_table(cursor=cursor, table_data=tbl_data)
            Write.end_paragraph(cursor)

        Lo.delay(delay)
        Write.append(cursor, f"Timestamp: {DateUtil.time_stamp()}")
        Lo.delay(delay)
        msg_result = MsgBox.msgbox(
            "Do you wish to save document?",
            "Save",
            boxtype=MessageBoxType.QUERYBOX,
            buttons=MessageBoxButtonsEnum.BUTTONS_YES_NO,
        )
        if msg_result == MessageBoxResultsEnum.YES:
            tmp = Path.cwd() / "tmp"
            tmp.mkdir(exist_ok=True)
            Lo.save_doc(doc, tmp / "table.odt")

        msg_result = MsgBox.msgbox(
            "Do you wish to close document?",
            "All done",
            boxtype=MessageBoxType.QUERYBOX,
            buttons=MessageBoxButtonsEnum.BUTTONS_YES_NO,
        )
        if msg_result == MessageBoxResultsEnum.YES:
            Lo.close_doc(doc=doc, deliver_ownership=True)
            Lo.close_office()
        else:
            print("Keeping document open")
    except Exception:
        Lo.close_office()
        raise

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
