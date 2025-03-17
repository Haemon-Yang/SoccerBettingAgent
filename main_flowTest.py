from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from graph import Workflow
from colorama import Fore, Style
from pprint import pprint
load_dotenv(dotenv_path="Agents/.env")

llm = ChatOpenAI(model="gpt-4o-mini")

workflow = Workflow(llm)
state = workflow.get_initial_state()

app = workflow.app

while True:
    user_input = input("Enter a user query: ")
    if user_input == "exit":
        print(Fore.RED + "Exiting..." + Style.RESET_ALL)
        break

    state.update({"user_query": user_input})

    for output in app.stream(state):
        pprint(output)
