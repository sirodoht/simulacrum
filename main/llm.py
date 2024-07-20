import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial

from django.conf import settings
from openai import OpenAI

from main import models

logger = logging.getLogger(__name__)


SYSTEM_PROMPT_TEMPLATE = """
If you are asked a question respond with your initial thoughts, emotions, actions you
might take, and things you might say. The following sentence describes you:

{persona_text}

This new policy is about to be voted for:

{policy}
"""

USER_PROMPT_TEMPLATE = """
How do you think of it? Answer in 1 sentence.
"""


def process_persona(client, user_prompt, policy, persona):
    try:
        system_prompt = (
            SYSTEM_PROMPT_TEMPLATE.replace("\n", " ")
            .strip()
            .format(persona_text=persona.text, policy=policy)
        )
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        logger.info(f"OpenAI API Request: {completion}")
        reaction_text = completion.choices[0].message.content
        return {
            "reaction_text": reaction_text,
            "persona_id": persona.id,
            "system_prompt": system_prompt,
        }
    except Exception as ex:
        logger.error(f"Error processing persona {persona.id}: {ex}")


def create_reactions(simulation, policy):
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    user_prompt = USER_PROMPT_TEMPLATE.replace("\n", " ").strip()

    persona_list = models.Persona.objects.all()
    with ThreadPoolExecutor(max_workers=10) as executor:
        process_persona_with_context = partial(
            process_persona, client, user_prompt, policy
        )
        future_list = [
            executor.submit(process_persona_with_context, persona)
            for persona in persona_list
        ]

        result_list = []
        for future in as_completed(future_list):
            try:
                result = future.result()
                if result:
                    result_list.append(result)
            except Exception as ex:
                logger.error(f"Thread raised an exception: {ex}")

    models.Reaction.objects.bulk_create(
        [
            models.Reaction(
                simulation=simulation,
                persona_id=result["persona_id"],
                system_prompt=result["system_prompt"],
                user_prompt=user_prompt,
                text=result["reaction_text"],
            )
            for result in result_list
        ]
    )


def process_sentiment(client, reaction):
    try:
        system_prompt = """
You are a sentiment analysis assitant. For every statement given, please
reply with one 'positive', 'neutral', or 'negative'. Always reply all
lowercase, no full stops, or other punctuation marks.
        """.replace("\n", " ")
        user_prompt = f"Statement: {reaction.text}"
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        logger.info(f"OpenAI API Request: {completion}")
        sentiment = completion.choices[0].message.content
        return {
            "reaction_id": reaction.id,
            "sentiment": sentiment,
        }
    except Exception as ex:
        logger.error(f"Error processing sentiment for reaction {reaction.id}: {ex}")


def generate_sentiment(simulation):
    client = OpenAI(api_key=settings.OPENAI_API_KEY)

    reaction_list = simulation.reaction_set.all()
    with ThreadPoolExecutor(max_workers=10) as executor:
        process_sentiment_with_context = partial(process_sentiment, client)
        future_list = [
            executor.submit(process_sentiment_with_context, reaction)
            for reaction in reaction_list
        ]

        result_list = []
        for future in as_completed(future_list):
            try:
                result = future.result()
                if result:
                    result_list.append(result)
            except Exception as ex:
                logger.error(f"Thread raised an exception: {ex}")

    updated_reactions = []
    for result in result_list:
        reaction = models.Reaction.objects.get(id=result["reaction_id"])
        reaction.sentiment = result["sentiment"]
        updated_reactions.append(reaction)
    models.Reaction.objects.bulk_update(updated_reactions, ["sentiment"])
