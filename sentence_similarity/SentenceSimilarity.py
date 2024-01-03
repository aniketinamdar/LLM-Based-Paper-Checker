from sentence_similarity import sentence_similarity

question_bank = "I'm happy"
answer_key = "I'm full of happiness"

model=sentence_similarity(model_name='distilbert-base-uncased',embedding_type='sentence_embedding')

score=model.get_score(question_bank,answer_key,metric="cosine")
print(score)
