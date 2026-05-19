import matplotlib.pyplot as plt

queries = ['Q1', 'Q2', 'Q3']

before = [2.5, 3.1, 2.8]
after = [0.8, 1.0, 0.7]

plt.figure(figsize=(8,5))

plt.plot(queries, before, marker='o', label='Before')
plt.plot(queries, after, marker='o', label='After')

plt.xlabel("Queries")
plt.ylabel("Execution Time (sec)")
plt.title("Performance Comparison")

plt.legend()

plt.savefig("reports/performance.png")

plt.show()
