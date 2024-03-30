#1
import re

text = "Contact emails are: john.doe@example.com and Jane.Doe@example.com."
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(emails)


#2
import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@(?!exclude\.com)[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)
print(emails)