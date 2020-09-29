funds = 918
num_of_servers = 20
cost_per_hour = 0.51
cost_per_day = cost_per_hour * 24
cost_per_month = cost_per_day * 30
print('Cost per day for 1 server: ${:.2f}'.format(cost_per_day))
print('Cost per month for 1 server: ${:.2f}'.format(cost_per_month))
print('Cost per day for {} servers: ${:.2f}'.format(num_of_servers, cost_per_day * num_of_servers))
print('Cost per month for {} servers: ${:.2f}'.format(num_of_servers, cost_per_month * num_of_servers))
print('1 server can last {:.0f} days'.format(funds / cost_per_day))
