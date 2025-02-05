from litellm import completion # type: ignore
import os

os.environ["GEMINI_API_KEY"] = "AIzaSywRgU"

def gemini():
    response = completion(
        modal="gemini/gemini-1.5-flash",
        messages=[{"content": "Hello, how are you?","role": "user"}],
    )
    
    print(response)