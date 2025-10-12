class RecentCounter:

    def __init__(self):
        self.curr_requests = 0
        self.curr_i = 0
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.curr_requests += 1
        if len(self.requests) != 1:
            while t - self.requests[self.curr_i] > 3000:
                self.curr_requests -= 1
                self.curr_i += 1
        return self.curr_requests
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)