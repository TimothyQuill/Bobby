## Bobby - The Pest / CCTV / Water / Electricity report summariser

The pipeline:

1. Download each report as a PDF file.
2. For each PDF file, do  
   I.   Use reader.py to convert the PDF to raw ASCII data  
   II.  Prefix the ASCII text with the relevant prompt in prompts.py  
   III. Send the text to the ChatGPT API. Concat the returned text to the final output.
3. Return the output, which contains all the ChatGPT converted reports as a single document.