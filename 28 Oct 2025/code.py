scores = [80,45,30,60,90]
print(f"Org Scores: {scores}")

for score in scores:
    if score < 50:
        scores.remove(score)

new_scores = [score for score in scores if score >= 50]

print(f"Result Scores: {scores}")
print(f"New Scores: {new_scores}")

