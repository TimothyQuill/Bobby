from arguments import args
import converter
from content import headings, prompts, reports
import reader

preface = 'Convert the following text to capital letters:'

responses = {}

reports = ['cctv']
for r in reports:
    try:
        txt = reader.pdf2txt(args.pdf_path+r+'_report.pdf')
        prompt = prompts[r].format(headings[r])+txt
        print(prompt)
        print('=======================================')
        responses[r] = converter.connect2gpt(prompt)
        #print(responses[r])
        #print('--------------------')
        #responses[r] = converter.connect2gpt(preface+responses[r])
        #print(responses[r])
    except FileNotFoundError:
        print('No report exists for', r)
report = reader.synthesizer(responses)
print(report)
