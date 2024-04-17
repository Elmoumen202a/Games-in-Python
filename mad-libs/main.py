def mad_libs():
    # Define your story template
    story = "Once upon a time, there was a {adjective} {noun} who {verb} {adverb}."

    # Prompt the user for inputs
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")

    # Insert user inputs into the story
    completed_story = story.format(adjective=adjective, noun=noun, verb=verb, adverb=adverb)

    # Display the completed story
    print(completed_story)

if __name__ == "__main__":
    mad_libs()
