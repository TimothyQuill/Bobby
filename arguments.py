import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--openai-key", default="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")
parser.add_argument("--model-engine", default="text-davinci-003")
parser.add_argument("--pdf-path", default="/Users/tim/Downloads/report_examples/")
args = parser.parse_args()
