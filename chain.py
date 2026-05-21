from prompt import prompt

from model import llm

from parser import parser

chain = prompt | llm | parser