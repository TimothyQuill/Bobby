import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--openai-key", default="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")
parser.add_argument("--model-engine", default="text-davinci-003")
parser.add_argument("--pdf-path", default="/Users/tim/Downloads/report_examples/")
args = parser.parse_args()
