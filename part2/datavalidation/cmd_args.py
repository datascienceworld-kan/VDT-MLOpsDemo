import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--test_path",
                    type=str,
                    help="Path to test dataset")

def main(args):
    print(f"Test path given is {args.test_path}")

if __name__=="__main__":
    args = parser.parse_args()
    main(args)