import argparse
import fastq


def main():
    argparser = argparse.ArgumentParser(
        description="Extract the sequences from a simple-fastq file")
    argparser.add_argument(
        "fastq",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()
    for _, seq in fastq.extract_reads(args.fastq):
        print(seq)


if __name__ == '__main__':
    main()
