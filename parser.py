from pydantic import BaseModel, Field

from langchain_core.output_parsers import PydanticOutputParser


class PostAnalysis(BaseModel):

    tone: str = Field(
        description="Tone of the post"
    )

    intent: str = Field(
        description="Intent of the post"
    )

    communication_style: str = Field(
        description="Communication style of the post"
    )

    summary: str = Field(
        description="Short summary of the post"
    )


parser = PydanticOutputParser(
    pydantic_object=PostAnalysis
)