import ollama

MODEL = "phi3"

def get_llm_answer(messages):
    response = ollama.chat(
        model = MODEL,
        messages = messages
    )
    print(response["message"]["content"])

if __name__ == "__main__":
    import time
    test_msgs = [
        {'role': 'user', 'content': 'please describe image with 5 adjective + noun in a list, for instance: ["beautiful girl", "cute woman", "red car", "crazy man", "blue sky"]', 'images': ['./xx.jpg']}
    ]
    start = time.time()
    get_llm_answer(test_msgs)
    end = time.time()
    print(end - start)