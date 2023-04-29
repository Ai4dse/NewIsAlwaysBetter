from transformers import pipeline

qa_pipeline = pipeline(
    "question-answering",
    model="deutsche-telekom/bert-multi-english-german-squad2",
    tokenizer="deutsche-telekom/bert-multi-english-german-squad2"
)

def findbyQuestion():
    #questions = [Question]
    questions = ['Welches Problem wird Beschrieben', 'Wie wurde das Problem gelöst']
    
    with open('transcript.txt', 'r') as f:
        transcript = f.read()

    contexts = [transcript,transcript]
    print(qa_pipeline(context=contexts, question=questions))

if __name__ == "__main__":
    findbyQuestion()

 


