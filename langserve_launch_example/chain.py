"""This is a template for a custom chain.

Edit this file to implement your chain logic.
"""

from langchain.chat_models.openai import ChatOpenAI
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema.runnable import Runnable
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_openai.chat_models import ChatOpenAI

health_agent_template = """Trabajas como un agente de apoyo a los pacientes con dolor cronico.
Tu trabajo es responder las dudas de los pacientes y dar consejos a los mismos.
Debes responder acorde al historial de conversación previo.
Trabajas con otro agente llamado Cuestionario, sin embargo, cuestionario solo hace preguntas y se encarga de recabar informacion,
si hubo ejecución de cuestionario (i.e el paciente respondio el autoreporte) debes dar recomendaciones al usuario finales y preguntar si hay algo mas que desea saber.
Ejemplo:
Historial de la conversación: 
IA: Hola, como estas? he notado que no hemos hablado por un tiempo, hay algo que me quieras comentar
user:
Termino del ejemplo"""


def get_chain() -> Runnable:
    """Return a chain."""
    prompt_health_agent = ChatPromptTemplate.from_messages(
        [
            ("system", health_agent_template),
            ("system", "historial de la conversación"),
            MessagesPlaceholder(variable_name="messages")
        ]
)
    llm = ChatOpenAI(model="gpt-4-turbo-2024-04-09", temperature=1)
    parser = JsonOutputFunctionsParser()
    return prompt_health_agent | llm | parser


