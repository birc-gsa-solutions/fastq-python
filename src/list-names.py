import argparse
import fastq


def main():
    argparser = argparse.ArgumentParser(
        description="Extract the names from a simple-fastq file")
    argparser.add_argument(
        "fastq",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()
    for name, _ in fastq.extract_reads(args.fastq):
        print(name)


if __name__ == '__main__':
    main()
