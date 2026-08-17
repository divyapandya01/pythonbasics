# Exercise 1: Encountering Data - Reading the News Article

# Define a Python function "read_article" and pass "text_file" as parameter
def read_article(text_file):

    # Open file in read mode
    f = open(text_file, "r")

    # Read contents
    contents = f.read()

    # Close file
    f.close()

    # Return contents
    return contents


# Exercise 2: Decoding the Cosmos - Extracting Key Topics

news_article = read_article("news_article.txt")

# Create a prompt
prompt = f"""
Read the contents of file {news_article}, and extract the key topics discussed in it. Provide exactly 3 key topics.

Each topic should not be more than 8 words.

Provide each topic in a new line.

Output Format:

topic_1

topic_2

topic_3
"""

response = get_llm_response(prompt)

# Print the response
print(response)


# Store the key topics in a list
key_topics = [
    "New Horizons Pluto flyby discoveries",
    "Pluto's active geology and icy surface",
    "Kuiper Belt objects and solar system formation"
]

print_formatted_list(key_topics)


# Exercise 3: The Poet's Palette - Organizing Your Topics

topics_to_use = [
    {
        "Topic 1": key_topics[0],
        "to_use": True
    },
    {
        "Topic 2": key_topics[1],
        "to_use": True
    },
    {
        "Topic 3": key_topics[2],
        "to_use": True
    }
]

print_formatted_list_of_dict(topics_to_use)


# Exercise 4: Cosmic Sonnets - Writing Your Space Poem

prompt = f"""
Using only the topics in this list: {topics_to_use},
write a poem about space exploration.

The poem must:
- Use ONLY these topics
- Be exactly 4 (four) lines (line)
"""

print(prompt)

poem = get_llm_response(prompt)

# Print your poem
print(poem)


# Exercise 5: Preserving the Verse - Saving Your Poem

# Define a Python function "save_to_file" and pass "contents_to_save" as parameter
def save_to_file(contents_to_save):

    f = open("poem.txt", "w")

    # Write "contents_to_save" in the file `poem.txt`
    f.write(contents_to_save)

    # Close the file
    f.close()
