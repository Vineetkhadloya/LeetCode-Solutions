
def uniqueEmails(emails):
    uniqueEmails = set()

    for e in emails:
        if e in uniqueEmails:
            continue
        else:
            uniqueEmails.add(e)

    return list(uniqueEmails)

emails = ["xyz@gmail.com","abc@gmail.com","xyz@gmail.com","vineet@gmail.com"]
emails = []
print(emails)
print(uniqueEmails(emails))