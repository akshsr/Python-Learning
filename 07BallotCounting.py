# List of votes (ballots)
polls = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice", "Charlie", "Alice", "Bob"]

candidates = []

votes = []
for person in polls:
    if person not in candidates:
        candidates.append(person)
        votes.append(1)
    else:
        candidates_index = candidates.index(person)
        votes[candidates_index] += 1

print(votes)

max_vote = 0
max_candidates = []
for i in range(len(votes)):
    if votes[i] > max_vote:
        max_vote = votes[i]
        candidates = candidates[i]


        max_candidates = []
        max_candidates.append(candidates)
    elif votes[i] == max_vote:
        candidates = candidates[i]
        max_candidates.append(candidates)

print('The max votes goes to: ')
print(*max_candidates, sep='/n')
print('This person has', str(max_vote),'votes.' )


