# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open('../Mail Merge Project Start/Input/Names/invited_names.txt') as file:
    names = file.readlines()
    clean_names = []
    for name in names:
        name = name.strip('\n')
        clean_names.append(name)
    print(clean_names)
    with open('../Mail Merge Project Start/Input/Letters/starting_letter.txt', mode='r') as f:
        mail = f.read()
        for clean_name in clean_names:
            mails = mail.replace('[name]',clean_name)
            with open(f'../Mail Merge Project Start/Output/ReadyToSend/{clean_name}', mode='w') as send:
                send.write(mails)

