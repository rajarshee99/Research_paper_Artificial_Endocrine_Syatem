# deep_personality_test.py

# Deep Personality Test (OCEAR Model)
# 5 Traits × 4 Questions = 20 Questions
# Scoring range: 4–20 for each trait

questions = [
    # Openness & Curiosity (O)
    ("I enjoy exploring new ideas, cultures, or perspectives.", "O"),
    ("I often reflect on abstract or philosophical topics.", "O"),
    ("I like experimenting with new approaches or experiences.", "O"),
    ("I am curious about why people think and behave the way they do.", "O"),

    # Conscientiousness & Self-Regulation (C)
    ("I make detailed plans and follow through with them.", "C"),
    ("I stay focused on tasks even when distracted or stressed.", "C"),
    ("I can control my impulses in emotionally charged situations.", "C"),
    ("I take responsibility for my actions and learn from mistakes.", "C"),

    # Extraversion & Social-Emotional Awareness (E)
    ("I feel energized and comfortable around people.", "E"),
    ("I can express my thoughts and feelings clearly in social settings.", "E"),
    ("I enjoy leading or participating actively in group activities.", "E"),
    ("I am aware of how my moods affect others in social interactions.", "E"),

    # Agreeableness & Empathy (A)
    ("I am considerate of other people’s feelings.", "A"),
    ("I seek to understand and support others without expecting rewards.", "A"),
    ("I trust others but also notice when someone may take advantage.", "A"),
    ("I reflect on how my actions impact those around me emotionally.", "A"),

    # Emotional Resilience & Authenticity (R)
    ("I recover from setbacks fairly quickly and learn from them.", "R"),
    ("I notice and reflect on my emotional reactions to difficult situations.", "R"),
    ("I act in ways that align with my core values, even when it’s difficult.", "R"),
    ("I strive to live a life that feels meaningful and true to myself.", "R"),
]

trait_names = {
    "O": "Openness & Curiosity",
    "C": "Conscientiousness & Self-Regulation",
    "E": "Extraversion & Social-Emotional Awareness",
    "A": "Agreeableness & Empathy",
    "R": "Emotional Resilience & Authenticity",
}

def interpret_trait(tag, score):
    if tag == "O":
        if score <= 7: return "Very Low: Prefers routine, avoids new ideas."
        elif score <= 11: return "Low: Practical, cautious with new experiences."
        elif score <= 15: return "Moderate: Balanced curiosity and reflection."
        elif score <= 18: return "High: Open-minded, enjoys new perspectives."
        else: return "Very High: Highly imaginative, philosophical, novelty-seeking."
    elif tag == "C":
        if score <= 7: return "Very Low: Disorganized, impulsive."
        elif score <= 11: return "Low: Sometimes responsible, inconsistent."
        elif score <= 15: return "Moderate: Reliable, decent self-control."
        elif score <= 18: return "High: Disciplined, structured, focused."
        else: return "Very High: Extremely organized, possibly perfectionistic."
    elif tag == "E":
        if score <= 7: return "Very Low: Reserved, prefers solitude."
        elif score <= 11: return "Low: Quiet, prefers small groups."
        elif score <= 15: return "Moderate: Balanced, enjoys people & alone time."
        elif score <= 18: return "High: Outgoing, expressive, socially confident."
        else: return "Very High: Extremely social, charismatic."
    elif tag == "A":
        if score <= 7: return "Very Low: Competitive, less empathetic."
        elif score <= 11: return "Low: Selectively cooperative, self-focused."
        elif score <= 15: return "Moderate: Generally kind, fair, sets boundaries."
        elif score <= 18: return "High: Warm, cooperative, empathetic."
        else: return "Very High: Extremely compassionate, selfless."
    elif tag == "R":
        if score <= 7: return "Very Low: Easily stressed, struggles with setbacks."
        elif score <= 11: return "Low: Sensitive, slow recovery, inconsistent."
        elif score <= 15: return "Moderate: Handles stress fairly well, reflective."
        elif score <= 18: return "High: Resilient, balanced, authentic."
        else: return "Very High: Strong inner stability, thrives under challenges."

def main():
    print("=== Deep Personality Test (OCEAR Model) ===")
    print("Rate each statement from 1 (Strongly Disagree) to 5 (Strongly Agree)\n")

    scores = {"O": 0, "C": 0, "E": 0, "A": 0, "R": 0}

    for i, (q, tag) in enumerate(questions, start=1):
        while True:
            try:
                ans = int(input(f"Q{i}. {q} (1-5): "))
                if 1 <= ans <= 5:
                    scores[tag] += ans
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input, enter a number 1–5.")

    print("\n=== Your Personality Profile ===")
    for tag in ["O", "C", "E", "A", "R"]:
        score = scores[tag]
        print(f"{trait_names[tag]}: {score}/20 → {interpret_trait(tag, score)}")

if __name__ == "__main__":
    main()
