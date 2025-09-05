from langchain_groq import ChatGroq
from vector_database import faiss_db
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate


# Step 1: setup LLM ( use deepseek r1 with groq)

# load_dotenv
load_dotenv()

llm_model=ChatGroq(model="deepseek-r1-distill-llama-70b")

# Step 2: retrive docs

def retrieve_docs(query):
    return faiss_db.similarity_search(query)

def get_context(documents):
    context="\n\n".join([doc.page_content for doc in documents])
    return context

# Step 3: answer question

custom_prompt_template="""
Use the pieces of the information provided in the context to answer user's question.
If you do not know the answer, just say that you do not know, do not try to make up an answer.
Do not provide anything out of the given context
Question: {question}
Context: {context}
Answer:
"""

def answer_query(documents, model, query):
    context=get_context(documents)
    prompt=ChatPromptTemplate.from_template(custom_prompt_template)
    chain=prompt | model
    return chain.invoke({"question": query, "context": context})

# question="If a government forbids the right to assemble peacefully which articles are violated and why?"
# retrieved_docs=retrieve_docs(question)
# print("AI Lawyer: ", answer_query(documents=retrieved_docs, model=llm_model, query=question))