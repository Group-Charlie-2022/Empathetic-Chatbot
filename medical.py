from interface import Routine
from WebScraping import file_uploader
import openai
import os

openai.api_key = os.getenv("OPENAI_KEY")

class Medical(Routine):
    
    @staticmethod
    def process(inp, history):
        response = openai.Answer.create(
            search_model="ada",
            model="curie",
            question= inp,
            file=file_uploader.fetch_id(),
            examples_context="Question: Who is most at risk of severe illness from COVID-19? Answer: People aged 60 years and over, and those with underlying medical problems like high blood pressure, heart and lung problems, diabetes, obesity or cancer, are at higher risk of developing serious illness. Hepatitis A is an inflammation of the liver caused by the hepatitis A virus (HAV). The virus is primarily spread when an uninfected (and unvaccinated) person ingests food or water that is contaminated with the faeces of an infected person.",
            examples=[["What has the most risk from getting COVID?", "People aged 60 years and over, and those with underlying medical problems like high blood pressure, heart and lung problems, diabetes, obesity or cancer."],["What is hepatitis?","Hepatitis A is an inflammation of the liver caused by the hepatitis A virus (HAV). The virus is primarily spread when an uninfected (and unvaccinated) person ingests food or water that is contaminated with the faeces of an infected person."]],
            max_rerank=10,
            max_tokens=100,
            stop=["\n", "<|endoftext|>"]
        )

        return response["answers"][0]

