from intent_suggestions import intent_suggestions
import pandas as pd

model = intent_suggestions.IntentSuggester(n=2)

# A hypotherical list of sentences and the emotions they convey
# lines = [
#     "I'm happy as it is sunny outside",
#     "I am sad as it is raining today",
#     "I am afraid of going out as it is very dark outside",
#     "Because he hurt me I am furious",
#     "It is very dark outside and I am fearful",
#     "Wow, this was a very shocking revelation",
#     "I feel guilty for eating so much yesterday",
# ]
# emotional_labels: list[str] = [
#     "happy",
#     "sad",
#     "anxious",
#     "angry",
#     "fear",
#     "surprise",
#     "guilt",
# ]
#
# # fitting the `n gram` model with the data and the corresponding labels
# model.fit(lines, emotional_labels)
#
# sentence: str = input("What is on your mind: ")
# prediction = model.predict(sentence)
#
# # d = { "emotions": ["e1", "e2", ..., "en"], "response": [r1, r2, ..., rn]}
# data = {"emotions": list(prediction.keys()), "response": list(prediction.values())}

data = pd.read_csv("./go_emotions_dataset.csv")

df = pd.DataFrame(data)
print(df)

# fig, ax = plt.subplots()
# ax.pie(data["response"], labels=data["emotions"])
# ax.set_title("Sport Popularity")
# plt.tight_layout()
# plt.show()
