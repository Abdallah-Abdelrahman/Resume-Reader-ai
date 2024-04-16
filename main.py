#!/usr/bin/env python3
'''The module define `Prompt` class that serves as interactive mode
chat prompt to obtain info about a pdf file
'''
import os
import cmd
import google.generativeai as genai
from pdfminer.high_level import extract_text
from google.auth import sys

# convo = model.start_chat()


class Prompt(cmd.Cmd):
    '''prompt'''
    prompt = '(User:) '

    def __init__(self):
        '''Initialze the model and prompt'''
        super().__init__()
        genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

        # Set up the model
        generation_config = {
          "temperature": 0.9,
          "top_p": 1,
          "top_k": 1,
          "max_output_tokens": 2048,
        }

        safety_settings = [
          {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
          {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
          {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
          {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
        ]

        self.model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                           generation_config=generation_config,
                                           safety_settings=safety_settings)

    def precmd(self, line):
        '''Runs before and command'''
        print('(Gemeni:) ', end='')
        sys.stdout.flush()
        return line

    def emptyline(self):
        """Handle empty line by doing nothing"""

    def do_quit(self, _):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, _):
        """End-of-file"""
        return True

    def default(self, line):
        '''ask gemeni and generate a response.
        based on the pdf file.

        Args:
            line: prompt to provide for gemini
        Notes:
            the function assumes there's a pdf file called cv.pdf
            feel free to change this to obtain some info about the the cv
        '''
        input_ = extract_text("cv.pdf").strip()
        resp = self.model.generate_content([line, input_], stream=True)
        for chunk in resp:
            print(chunk.text)


if __name__ == '__main__':
    Prompt().cmdloop()
