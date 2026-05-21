from langchain_core.prompts import PromptTemplate

from parser import parser

template = """
You are an expert social media analyst.

Analyze the given social media post.

Identify:
1. Tone
2. Intent
3. Communication Style
4. Summary

Return the output in valid JSON format.

{format_instructions}

Social Media Post:
{post}
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["post"],
    partial_variables={
        "format_instructions":
        parser.get_format_instructions()
    }
)