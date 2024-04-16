# Simple Resume Prompt

The application parses a pdf file, and feed the context to google `Gemini` AI to provide you with some context about the cv.

## Installation:
+ clone the repo
+ head over to the project and initialize your environment variable
   - run `python3 -m venv <venv-name>`
   - run  `source <venv-name>/bin/activate`
   - run `pip install -r requirements.txt`
+ head over to [google](https://aistudio.google.com/app/apikey) and generate an api key, and put it in your environment variable under the name `GOOGLE_API_KEY`.

## How to use:

The application assumes there's a `cv.pdf` in your project tree, feel free to change that.</b>
run ` GOOGLE_API_KEY=<your-api-key> python3 main.py` then you'll have your prompt initialized, you can ask the AI anyhting about the provided resume.
