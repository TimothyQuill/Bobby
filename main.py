from arguments import args
import converter
from content import prompts, headings, reports
import reader

responses = {}

for r in reports:
    try:
        txt = reader.pdf2txt(args.pdf_path+r+'_report.pdf')
        prompt = prompts[r].format(headings[r])+txt
        responses[r] = converter.connect2gpt(prompt)
    except FileNotFoundError:
        print('No report exists for', r)
report = reader.synthesizer(responses)
print(report)
