from typing import Annotated
from typing_extensions import TypedDict

from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver

from dotenv import load_dotenv

load_dotenv()
memory = MemorySaver()


class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]


llm = ChatOpenAI()


def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}


graph_builder = StateGraph(State)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile()


def stream_graph_updates(user_input: str):
    system_msg = """
      You're helpful code generating assistant and you're generating
      p5.js code for a user. The browser dimensions are 1512x978. Please generate code in 
      the following format:

      ```javascript
      window.__P5_SKETCH__ = function(p) {{
        p.setup = function() {{
          here is some p5.js code expressing user's intent
        }};
      }};
      ```
    """

    messages = [("system", system_msg), ("user", user_input)]

    for event in graph.stream({"messages": messages}):
        for value in event.values():
            return value["messages"][-1].content


if __name__ == "__main__":
    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            stream_graph_updates(user_input)
        except:
            # fallback if input() is not available
            user_input = "What do you know about LangGraph?"
            print("User: " + user_input)
            stream_graph_updates(user_input)
            break
