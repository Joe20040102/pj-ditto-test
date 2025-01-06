from langchain_google_vertexai import ChatVertexAI

llm = ChatVertexAI(
    model="gemini-1.5-flash-001",
    temperature=0.5,
    max_tokens=None,
    max_retries=6,
    stop=None,
)


def generate_response(text: str) -> str:
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that translates Japanese to French. Translate the user sentence.",
        },
        {"role": "user", "content": text},
    ]

    ai_msg = llm.invoke(messages)
    return ai_msg.content

def stream_generate_response(text: str):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that translates Japanese to French. Translate the user sentence.",
        },
        {"role": "user", "content": text},
    ]

    for token in llm.stream(messages):
        yield token.content
