import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--openai-key", default="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")
parser.add_argument("--model-engine", default="text-davinci-003")
parser.add_argument("--pdf-path", default="/Users/tim/Downloads/report_examples/")
args = parser.parse_args()
