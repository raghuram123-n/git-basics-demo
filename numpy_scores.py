import numpy as np

# -----------------------------
# Task 1 — Generate and Inspect
# -----------------------------

np.random.seed(42)

# Generate random scores (5 students × 4 subjects)
scores = np.random.randint(50, 101, size=(5, 4))

print("Original Scores:\n", scores)

# 3rd student, 2nd subject
print("\n3rd student, 2nd subject:")
print(scores[2, 1])

# Last 2 students (all subjects)
print("\nLast 2 students:")
print(scores[-2:, :])

# First 3 students, subjects 2 and 3
print("\nFirst 3 students (Subjects 2 & 3 only):")
print(scores[:3, 1:3])


# -----------------------------
# Task 2 — Analysis
# -----------------------------

# Column-wise mean (average per subject)
column_mean = np.round(scores.mean(axis=0), 2)
print("\nColumn-wise Mean:", column_mean)

# Add curve using broadcasting
curve = np.array([5, 3, 7, 2])
curved_scores = scores + curve

# Ensure no score exceeds 100
curved_scores = np.clip(curved_scores, None, 100)

print("\nCurved Scores:\n", curved_scores)

# Row-wise max
row_max = curved_scores.max(axis=1)
print("\nBest Subject Score Per Student:", row_max)


# -----------------------------
# Task 3 — Normalization
# -----------------------------

# Min-Max normalization per row
row_min = curved_scores.min(axis=1, keepdims=True)
row_max = curved_scores.max(axis=1, keepdims=True)

normalized = (curved_scores - row_min) / (row_max - row_min)

print("\nNormalized Scores:\n", normalized)

# Find highest value index
max_index = np.unravel_index(np.argmax(normalized), normalized.shape)
print("\nHighest Normalized Value at (Student, Subject):", max_index)

# Scores strictly above 90
above_90 = curved_scores[curved_scores > 90]
print("\nScores strictly above 90:", above_90)