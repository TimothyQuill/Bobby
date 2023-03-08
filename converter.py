from arguments import args
import openai

def connect2gpt(prompt):
    openai.api_key = args.openai_key
    completion = openai.Completion.create(
        engine=args.model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.0
    )

    return completion.choices[0].text
