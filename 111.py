initial_tasks = [(0, 2), (3, 6), (3, 5), (4, 8)]#query 1, 6 ->3

# initial_tasks = [(0, 1), (2, 3), (4, 5), (7, 8)]#query 1, 10 ->1



class CalculateTasks:
    def __init__(self, tasks):
        self.tasks = tasks


    def add(self, start, end):
        pass

    def query(self, start_time, end_time):
        new = []
        for i in self.tasks:
            if start_time > i[1] or end_time < i[0]:
                continue
            s = i[0] if i[0] >= start_time else start_time
            e = i[1] if i[1] <= end_time else end_time
            for j in range(s, e):
                new.append(j)

        often = max(new, key=new.count)
        max_count = new.count(often)
        return max_count


x = CalculateTasks(initial_tasks)

print(x.query(2, 3))