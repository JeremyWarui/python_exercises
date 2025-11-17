# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
for word in headlines:
    if len(news_ticker) + len(word) + 1 > 140:
        remaining_space = 140 - len(news_ticker) - 1
        if remaining_space > 0:
            news_ticker += " " + word[:remaining_space]
        break
    else:
        if news_ticker:
            news_ticker += " "
        news_ticker += word 

print(news_ticker)