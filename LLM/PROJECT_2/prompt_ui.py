import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
import streamlit as st


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"))

model = ChatHuggingFace(llm=llm)
st.header("Research assistant")


paper_input=st.selectbox(
    "Select Research Paper Name",["Attention Is All You Need",
    "BERT:Pre-training of Deep Bodirectional Transformers",
    "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis", 
    "NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis"])

style_input=st.selectbox("Select Explaination Style ",["Begineer-Friendly","Technical","Code-Oriented","Mathematical"])

length_input=st.selectbox("Select Explaination Length ",["Short(1-2 paragraphs)","Medium(3-4 paragraphs)","Long(5 paragraphs)"])


# template

template=PromptTemplate(
    template="""
please summarize the research paper titled "{paper_input}" with the 
following specifications:
Explanation style:{style_input} 
Explanation length:{length_input}
1. Mathematical Details:
  - Include relevant equations, formulas, and mathematical concepts used in the paper.
 2. Analogies:
  -Use relatable analogies to simplify complex ideas.

if certain concepts are not present in the paper, please respond with "Not present in the paper" for that section.
ensure the summary  is clear , accurate and aligned with the provided style and length.
""",
input_variables=["paper_input","style_input","length_input"])

prompt=template.invoke({
    'paper_input': paper_input,
    'style_input': style_input, 
    'length_input': length_input})


if st.button("Submit"):
    result = model.invoke(prompt)
    st.write(result.content)
