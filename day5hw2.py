# Task 1: Product Review Analysis
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

for i in reviews:
    new_review = i.replace("good", "GOOD").replace("bad","BAD")\
    .replace("excellent", "EXCELLENT").replace("Poor", "POOR")\
    .replace("average", "AVERAGE")
    print(new_review)

# Task 2: Sentiment tally

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "Poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

positive_count = []
negative_count = []

def positive_counter():
    new_string = " ".join(reviews)
    for i in positive_words:
        if i in new_string:
            positive_count.append(i)
    print(f"There were a total of {len(positive_count)} positive words.")


def negative_counter():
    new_string = " ".join(reviews)
    for i in negative_words:
        if i in new_string:
            negative_count.append(i)
    print(f"There were a total of {len(negative_count)} negative words.")


def review_summary():
    for i in reviews:
        if len(i) < 30:
            print(i)
        else:
            last_space = i[:30].rfind(" ")
            print(i[:last_space] + " ...")

positive_counter()
negative_counter()
review_summary()
