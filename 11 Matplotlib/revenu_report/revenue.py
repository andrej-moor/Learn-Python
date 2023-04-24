import matplotlib.pyplot as plt

revenue_2020 = [1000, 2000, 3000, 2500, 2400, 2700, 2800, 2900, 3200, 2000, 2300, 3100]
revenue_2021 = [2300, 2500, 2800, 2400, 2600, 2700, 2900, 3200, 3000, 2000, 2300, 2400]
month = [1,2,3,4,5,6,7,8,9,10,11,12]

plt.style.use('seaborn-dark')
fig,ax = plt.subplots()

plt.xticks(month)
ax.plot(month,revenue_2020, label = "2020")
ax.plot(month,revenue_2021, label = "2021")

plt.legend()
ax.set_title("Revenue by Month")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue in Euro")

plt.show()
