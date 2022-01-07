#!/bin/python3

import argparse
import csv

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Check if new the findings were not already found'
    )
    parser.add_argument(
        '-f', '--oldfindings',
        help="Files containing old finding",
        required=True
    )

    parser.add_argument(
        '-n', '--newfindings',
        help="Files containing new findings",
        required=True
    )

    parser.add_argument(
        '-o', '--output',
        help="Output file to save results",
        required=True
    )

    args = parser.parse_args()

    output = open(args.output, "w", newline='')
    writer = csv.writer(output)

    my_file = open(args.oldfindings, "r")
    old_findings = my_file.read().split("\n")

    with open(args.newfindings) as new_findings:
        for new_finding in new_findings:
            check = False
            for old_finding in old_findings:
                if new_finding.strip() == old_finding.strip():
                    check = True

            if not check:
                writer.writerow([new_finding.rstrip()])

    output.close()

