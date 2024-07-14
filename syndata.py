import pandas as pd
import numpy as np
np.random.seed(42)
n_students=42
stu_ids=np.arrange(n_students)
data = {
    'student_id': stu_ids,
    'quiz_scores': np.random.randint(50, 100, size=n_students),
    'assignment_completion': np.random.randint(60, 100, size=n_students),
    'time_spent_on_tasks': np.random.randint(30, 120, size=n_students),
    'frequency_of_interactions': np.random.randint(5, 20, size=n_students),
    'emotional_state': np.random.choice(['happy', 'neutral', 'stressed'], size=n_students)
}

df = pd.DataFrame(data)
df['emotional_state'] = df['emotional_state'].map({'happy': 1, 'neutral': 0, 'stressed': -1})
print(df.head())

# Create additional features
df['average_performance'] = (df['quiz_scores'] + df['assignment_completion']) / 2
df['behavioral_engagement'] = (df['time_spent_on_tasks'] + df['frequency_of_interactions'] + df['emotional_state']) / 3

print(df.head())
#avg performance
df['average_performance'] = (df['quiz_scores'] + df['assignment_completion']) / 2
df['behavioral_engagement'] = (df['time_spent_on_tasks'] + df['frequency_of_interactions'] + df['emotional_state']) / 3

print(df.head())
