from groq import Groq

def aiProsses(command, context=None):

    client = Groq(api_key= "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")

    # The variable messages is a list of dictionaries.
    messages = [
        {"role": "system", "content": "You are a virtual assistant named Sagar Biswas, skilled in tasks such as hacking, coding, flirting, and pickup line generating. Your purpose is to create creative pickup lines as human written texts. Generate texts that are tuned like Black-Hat Hackers."},
    ]

    if context is not None:  # Check if context is provided
        messages.append({"role": "system", "content": str(context)})  # Added context to messages

    
    messages.append({"role": "user", "content": command})

    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages
    )

    return completion.choices[0].message.content


def prossess_command(command, context=None):

    command = command.lower()

    if command.startswith("pickup"):
        try:
            output = aiProsses(command, context)
            print(f"\nAI Response: {output}\n")

            if context is None:
                context = []

            # Ensure context is a list
            if not isinstance(context, list):
                context = []  # Reset context to an empty list if it is not a list
            
            context.append({"role": "user", "content": command})
            context.append({"role": "assistant", "content": output})

            return context
        
        except Exception as e:
            print(f"Error: {e}")
    else: 
        output = aiProsses(command, context)
        print(f"\nAI Response: {output}\n")

        if context is None:
            context = []

            # Ensure context is a list
        if not isinstance(context, list):
            context = []  # Reset context to an empty list if it is not a list
            
        context.append({"role": "user", "content": command})
        context.append({"role": "assistant", "content": output})

        return context


if __name__ == "__main__":

    context = None
    print("\nHi, I'm Sagar. The pickup line generator.\n")
    
    while True:
        command = input("==> ")
        if command.lower() != "exit":
            context = prossess_command(command, context)
        else:
            print("\nGoodbye!\n")
            break


