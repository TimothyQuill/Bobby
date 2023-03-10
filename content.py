
reports = ['cctv', 'electricity', 'water']

headings = {
    'cctv':         'Plumbing Report / CCTV Inspection',
    'electricity':  'Electrical Safety & Compliance',
    'water':        'Water Report'
}

prompts = {
    'cctv':         'Use the following prompts to format the report: \n'
                    '- Inspection Date \n'
                    '- Inspection Location/Address \n'
                    '- Scope, Limitations, Exclusions and Definitions of Inspection and Report \n'
                    '- Limitations and Conditions of Inspection/Report \n'
                    '- Results of Inspection (specific to the type of inspection conducted) \n'
                    '- Detailed Description of Findings \n'
                    '- Overall Condition/Assessment \n'
                    '- Recommendations/Next Steps \n'
                    '- Any Additional Notes or Observations \n'
                    'Break it all into sections and sub sections using bullet points! \n'
                    '***** \n',
    'electricity':  '',
    'water':        ''
}
