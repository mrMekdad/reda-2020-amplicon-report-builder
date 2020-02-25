import argparse
from amplicon_report_builder.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Report generator for amplicon runs with per-sample status tables and markdown output.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
