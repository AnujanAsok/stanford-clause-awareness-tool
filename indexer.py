from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader('data').load_data()
index = GPTVectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
questions = ["What was Rick's girlfriend's name?",
             "How did Jose and Amanda become friends",
             "Summarize each of the characters in the story",
             ]

for question in questions:
    print(question)
    response = query_engine.query(question)
    print(response)