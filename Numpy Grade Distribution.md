```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
grades = np.random.randint(0, 101, size=(100,4))

student_averages = np.mean(grades, axis = 1)
course_max = np.max(grades, axis=0)
course_min = np.min(grades, axis=0)  
overall_average = np.mean(grades)
course_std = np.std(grades, axis=0)

print("Average grade for each student:", student_averages)
print("Highest grade for each course:", course_max)
print("Lowest grade for each course:", course_min)
print("Overall average grade for all students:", overall_average)
print("Standard deviation for each course:", course_std)

high_achievers = grades[np.all(grades > 90, axis =1)]

if len(high_achievers) >= 1:
     print("Students with all grades above 90:\n", high_achievers)
else:
    print("No students have all grades above 90.")

for i in range(grades.shape[1]):
    plt.hist(grades[:, i], bins=10, alpha=0.5, label=f'Course {i+1}')


plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.title('Grade Distribution')
plt.legend()

plt.show()
```


![Numpy Grade Distribution](./numpy_grade_distribution.png)


