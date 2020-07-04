class Salary:
    def __init__(self, working_days_per_m, working_hours_per_d, working_months_per_y):
        self.working_days_per_m = working_days_per_m
        self.working_hours_per_d = working_hours_per_d
        self.working_months_per_y = working_months_per_y

    def yearly_salary(self, salary_per_m):
        return salary_per_m * self.working_months_per_y

    def mountly_salary(self, salary_per_m):
        return salary_per_m

    def daily_salary(self, salary_per_m):
        return salary_per_m / self.working_days_per_m

    def hourly_salary(self, salary_per_m):
        return (salary_per_m / self.working_days_per_m) - self.working_hours_per_d
