import time

def delay(seconds):
    time.sleep(seconds)

def delay_characters(text, seconds):
    for char in text:
        print(char, end='', flush=True)
        delay(seconds)
    print()

lyrics = [
    "And I'm off to the races,",  
    "Cases of Bacardi chasers",
    "Chasing me all over town",
    "'Cause he knows I'm wasted,",
    "Facing time again in Rikers",
    "Island and I won't get out.",
    "Because I'm crazy,",
    "baby,",
    "I need you to come here",
    "And save me.",
    "I'm your little scarlet starlet,",
    "Singing in the garden,",
    "Kiss me on my open mouth",
    "Ready for you."
]

delays = [
    0.06,
    0.07,
    0.08,
    0.05,
    0.07,
    0.09,
    0.1,
    0.2,
    0.06,
    0.07,
    0.07,
    0.06,
    0.08,
    0.07 
]

line_delays = [
    0.05,
    0.05,
    0.6,
    0.05,
    0.05,
    0.07,
    0.3,
    0.4,
    0.03,
    0.05,
    0.06,
    0.06,
    0.2,
    0.05 
]

for line, delay_time, line_delay in zip(lyrics, delays, line_delays):
    delay_characters(line, delay_time)
    delay(line_delay)