# coding: utf-8
import argparse
import sys
import os
from pathlib import Path
from cmds import uno_lnk
from src.build.build import Builder, BuilderArgs

# region parser
# region        Create Parsers


def _create_parser(name: str) -> argparse.ArgumentParser:
    return argparse.ArgumentParser(description=name)


# endregion     Create Parsers

# region        process arg command
def _args_cmd_link(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-a",
        "--add",
        help="Add uno links to virtual environment.",
        action="store_true",
        dest="add",
        default=False,
    )
    parser.add_argument(
        "-r",
        "--remove",
        help="Remove uno links to virtual environment.",
        action="store_true",
        dest="remove",
        default=False,
    )


def _args_cmd_build(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-c",
        "--config",
        help="Json config file that contains build info.",
        action="store",
        dest="config_json",
        required=True,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="If True some print statements will be made in the terminal.",
        action="store_true",
        dest="verbose",
        default=False,
    )
    embed_grp = parser.add_argument_group()
    embed_grp.add_argument(
        "-e",
        "--embed",
        help="If True script embeded script will be embed in a doc.",
        action="store_true",
        dest="embed",
        default=False,
    )
    embed_grp.add_argument(
        "-s",
        "--embed-src",
        help="Source document to embed script into. If omitted then default to interanl odt file.",
        action="store",
        dest="embed_src",
        default=None,
    )

def _args_action_cmd_link(
    a_parser: argparse.ArgumentParser, args: argparse.Namespace
) -> None:
    if not (args.add or args.remove):
        a_parser.error("No action requested, add --add or --remove")
    if args.add:
        uno_lnk.add_links()
    elif args.remove:
        uno_lnk.remove_links()


def _args_action_cmd_build(
    a_parser: argparse.ArgumentParser, args: argparse.Namespace
) -> None:
    bargs = BuilderArgs(
        config_json=args.config_json,
        embed_in_doc=bool(args.embed),
        embed_doc=args.embed_src,
        allow_print=bool(args.verbose),
    )
    builder = Builder(args=bargs)
    _valid = builder.build()
    if _valid == False:
        print("Build Failed")
    else:
        print("Build Success")


def _args_process_cmd(
    a_parser: argparse.ArgumentParser, args: argparse.Namespace
) -> None:
    if args.command == "cmd-link":
        _args_action_cmd_link(a_parser=a_parser, args=args)
    elif args.command == "build":
        _args_action_cmd_build(a_parser=a_parser, args=args)
    else:
        a_parser.print_help()


# endregion        process arg command
# endregion parser


def _main():
    # for debugging
    # args = "build -e -c src/examples/message_box/config.json"
    args = "build -e --config src/examples/input_box/config.json --embed-src src/examples/input_box/inputbox.odt"
    sys.argv.extend(args.split())
    main()


def main():
    os.environ["project_root"] = str(Path(__file__).parent)
    parser = _create_parser("main")
    subparser = parser.add_subparsers(dest="command")
    cmd_link = subparser.add_parser(
        name="cmd-link", help="Add/Remove links in virtual environments to uno files."
    )
    cmd_build = subparser.add_parser(name="build", help="Build a script")

    _args_cmd_link(parser=cmd_link)
    _args_cmd_build(parser=cmd_build)

    # region Read Args
    args = parser.parse_args()
    # endregion Read Args
    _args_process_cmd(a_parser=parser, args=args)


if __name__ == "__main__":
    main()
