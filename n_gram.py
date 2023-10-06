from intent_suggestions import intent_suggestions

model = intent_suggestions.IntentSuggester(n=2)

items = ["I'm happy because its sunny outside", "I'm feeling sad bacuse it is raining"]
labels = ["happy", "sad"]

model.fit(items, labels)

print(model.predict("It's sunny outside"))
