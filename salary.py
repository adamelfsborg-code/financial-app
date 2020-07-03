class Salary:
    def __init__(self, salary_per_m, working_days_per_m, working_hours_per_d, working_mounts_per_y):
        self.salary_per_m = salary_per_m
        self.working_days_per_m = working_days_per_m
        self.working_hours_per_d = working_hours_per_d
        self.working_mounts_per_y = working_mounts_per_y

    def __int__(self):
        return self.salary_per_m

    def yearly_salary(self):
        return self.salary_per_m * self.working_mounts_per_y

    def mountly_salary(self):
        return self.salary_per_m

    def daily_salary(self):
        return self.salary_per_m / self.working_days_per_m

    def hourly_salary(self):
        return (self.salary_per_m / self.working_days_per_m) - self.working_hours_per_d

s = Salary(2000, 30, 8, 12)
print(int(s))
