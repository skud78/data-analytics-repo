import time

class TokenBucket:
    def __init__(self, capacity, refill_rate_per_second):
        self.capacity = capacity
        self.refill_rate_per_second = refill_rate_per_second
        self.tokens = capacity
        self.last_refill_timestamp = time.time()

    def allow_request(self):
        self.refill()
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False

    def refill(self):
        now = time.time()
        elapsed = now - self.last_refill_timestamp
        tokens_to_add = int(elapsed * self.refill_rate_per_second)

        if tokens_to_add > 0:
            self.tokens = min(self.capacity, self.tokens + tokens_to_add)
            self.last_refill_timestamp = now

if __name__ == "__main__":
    bucket = TokenBucket(5, 1)  # capacity of 5 tokens, refills 1 token per second

    for i in range(10):
        allowed = bucket.allow_request()
        print(f"Request {i}: {'Allowed' if allowed else 'Blocked'}")
        time.sleep(0.5)  # simulate 0.5 second between requests