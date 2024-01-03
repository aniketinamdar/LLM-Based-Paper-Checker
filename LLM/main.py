from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def GetLlamaResponse(q_bank, a_key):
    llm = CTransformers(model='LLM/model/llama-2-7b-chat.ggmlv3.q8_0.bin', 
                        model_type='llama',
                        config={'max_new_tokens':256,
                                'temperature':0.01})
    template_text = """
    Compare the student's response with the key answer and evaluate the similarity. 

    Student's Response: "{q_bank}"
    Key Answer: "{a_key}"

    Based on the comparison, assign a score on a scale of 0-100 that reflects the degree of similarity between the student's response and the key answer. A score of 100 indicates a perfect match, while a score of 0 indicates no similarity.
    """.format(q_bank=q_bank, a_key=a_key)

    response = llm(template_text)
    return response


question_bank = "I'm happy"
answer_key = "I'm full of happiness"

print(GetLlamaResponse(question_bank, answer_key))
