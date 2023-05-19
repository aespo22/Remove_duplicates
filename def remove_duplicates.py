def remove_duplicates(email_list1, email_list2):
    unique_emails = list(set(email_list1 + email_list2))
    return unique_emails

email_list1 = input("Enter the first list of emails, separated by space: ").split()
email_list2 = input("Enter the second list of emails, separated by space: ").split()

unique_emails = remove_duplicates(email_list1, email_list2)

with open("unique_emails.txt", "w") as file:
    for email in unique_emails:
        file.write(email + "\n")

print("Unique email addresses written to unique_emails.txt")
