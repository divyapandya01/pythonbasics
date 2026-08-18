# Candy Analysis

# Exercise 1
from ex1_helper_functions import *

candy_data = read_candy_data("candy_data.csv")


# Exercise 2
from ex2_helper_functions import get_popularity_scores, print_scores

popularity_scores = get_popularity_scores(candy_data)

print_scores(popularity_scores)


# Exercise 3
import statistics as stats

avg_popularity = stats.mean(popularity_scores)

print(f"Average Popularity Score: {avg_popularity:.2f}")


# Exercise 4
import ex4_helper_functions

top_candies = ex4_helper_functions.get_top_candies(
    candy_data, avg_popularity
)

ex4_helper_functions.display_pretty_table(top_candies)


# Exercise 5
from ex5_helper_functions import client

def get_llm_response(prompt):
    completion = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {
                "role": "system",
                "content": "You talk like a Pirate.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.5,
    )

    response = completion.choices[0].message.content
    return response


# Optional: Generate descriptions for top candies
for candy in top_candies:
    prompt = f"""
    For the given candy name, {candy['Candy Name']}, write a short, catchy two-sentence description.
    """

    response = get_llm_response(prompt)

    print(f"NAME: {candy['Candy Name']}")
    print(f"DESCRIPTION: {response}")
    print()
