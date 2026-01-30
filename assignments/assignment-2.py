 # WhatsApp Chat Data Analysis

n = int(input("Enter the no of message: "))
data = {}

for i in range(n):
    name, msg = input().split(':')
    msg = msg.strip()
    if name in data:
        data[name].append(msg)
    else:
        data[name] = [msg]

print(data)

choices = {
    1:'Count total number of messages',
    2:'Identify unique users in the chat',
    3:'Count total words in the chat',
    4:'Calculate average words per message',
    5:'Find the longest message sent',
    6:'Find the most active user',
    7:'Get message count for a specific user',
    8:'Find the most frequently used word by a specific user',
    9:'Retrieve the first and last message sent by a user',
    10:'Check if a user is present in the chat',
    11:'Find commonly repeated words',
    12:'Reserved',
    13:'Identify the user with the longest average message length',
    14:'Count how many messages mention a specific user',
    15:'Remove duplicate messages',
    16:'Sort messages alphabetically',
    17:'Extract all questions asked in the chat',
    18:'Calculate the reply ratio between two users',
    19:'Check for deleted messages',
    20:'Exit'
}

while True:
    for i in choices:
        print(f'{i}, {choices[i]}')

    ch = int(input("Enter the choice: "))

    if ch == 1:
        count = 0
        for i in data:
            count += len(data[i])
        print("Total Number of messages:", count)

    elif ch == 2:
        print("Unique users in chat:")
        print(list(data.keys()))

    elif ch == 3:
        total_words = 0
        for i in data:
            for msg in data[i]:
                total_words += len(msg.split())
        print("Total words:", total_words)

    elif ch == 4:
        total_words = 0
        total_msgs = 0
        for i in data:
            total_msgs += len(data[i])
            for msg in data[i]:
                total_words += len(msg.split())
        avg = total_words / total_msgs
        print("Average words per message:", round(avg, 2))

    elif ch == 5:
        longest = ""
        user_name = ""
        for i in data:
            for msg in data[i]:
                if len(msg) > len(longest):
                    longest = msg
                    user_name = i
        print("Longest message:", f"{user_name}: {longest}")

    elif ch == 6:
        max_user = ""
        max_count = 0
        for i in data:
            if len(data[i]) > max_count:
                max_count = len(data[i])
                max_user = i
        print(f"Most active user: {max_user} ({max_count} messages)")

    elif ch == 7:
        u = input("Enter username: ")
        if u in data:
            print(f"Messages sent by {u}: {len(data[u])}")
        else:
            print("User not found.")

    elif ch == 8:
        u = input("Enter username: ")
        if u not in data:
            print("User not found.")
        else:
            freq = {}
            for msg in data[u]:
                for w in msg.lower().split():
                    freq[w] = freq.get(w, 0) + 1
            most = max(freq, key=freq.get)
            print("Most frequent word:", most)

    elif ch == 9:
        u = input("Enter username: ")
        if u not in data:
            print("User not found.")
        else:
            print("First message:", f"{u}: {data[u][0]}")
            print("Last message:", f"{u}: {data[u][-1]}")

    elif ch == 10:
        u = input("Enter username: ")
        if u in data:
            print(f"User '{u}' is present.")
        else:
            print(f"User '{u}' not found.")

    elif ch == 11:
        from collections import Counter
        all_words = []
        for i in data:
            for msg in data[i]:
                all_words.extend(msg.lower().split())
        freq = Counter(all_words)
        repeated = {w for w in freq if freq[w] > 1}
        print("Common repeated words:", repeated)

    elif ch == 12:
        print("Reserved Option")

    elif ch == 13:
        best_user = ""
        best_avg = 0
        for i in data:
            avg = sum(len(msg.split()) for msg in data[i]) / len(data[i])
            if avg > best_avg:
                best_avg = avg
                best_user = i
        print(f"User with longest avg message: {best_user} ({round(best_avg,2)} words)")

    elif ch == 14:
        name = input("Enter name to search: ").lower()
        count = 0
        for i in data:
            for msg in data[i]:
                if name in msg.lower():
                    count += 1
        print(f"Messages mentioning '{name}':", count)

    elif ch == 15:
        seen = set()
        unique = []
        for i in data:
            for msg in data[i]:
                if msg not in seen:
                    seen.add(msg)
                    unique.append(msg)
        print("Unique messages count:", len(unique))
        print(unique)

    elif ch == 16:
        all_msgs = []
        for i in data:
            for msg in data[i]:
                all_msgs.append(msg)
        print("Messages sorted A–Z:")
        for m in sorted(all_msgs):
            print(m)

    elif ch == 17:
        qns = []
        for i in data:
            for msg in data[i]:
                if '?' in msg:
                    qns.append(msg)
        print("Questions:")
        for q in qns:
            print(q)

    elif ch == 18:
        u1 = input("Enter first user: ")
        u2 = input("Enter second user: ")
        count = 0
        for i in data:
            for msg in data[i]:
                if i == u2 and u1.lower() in msg.lower():
                    count += 1
        print(f"Reply ratio from {u2} to {u1}: {count}")

    elif ch == 19:
        deleted = 0
        for i in data:
            for msg in data[i]:
                if msg == "This message was deleted":
                    deleted += 1
        print("Deleted messages found:", deleted)

    elif ch == 20:
        print("End of the program")
        break

    else:
        print("Invalid Choices")