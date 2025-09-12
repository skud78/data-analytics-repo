import java.util.concurrent.atomic.AtomicInteger;

public class TokenBucket {
    private final int capacity;
    private final int refillRatePerSecond;
    private int tokens;
    private long lastRefillTimestamp;

    public TokenBucket(int capacity, int refillRatePerSecond) {
        this.capacity = capacity;
        this.refillRatePerSecond = refillRatePerSecond;
        this.tokens = capacity;
        this.lastRefillTimestamp = System.nanoTime();
    }

    public synchronized boolean allowRequest() {
        refill();

        if (tokens > 0) {
            tokens--;
            return true;
        }

        return false;
    }

    private void refill() {
        long now = System.nanoTime();
        long elapsedTime = now - lastRefillTimestamp;
        int tokensToAdd = (int) ((elapsedTime / 1_000_000_000.0) * refillRatePerSecond);

        if (tokensToAdd > 0) {
            tokens = Math.min(capacity, tokens + tokensToAdd);
            lastRefillTimestamp = now;
        }
    }

    public static void main(String[] args) throws InterruptedException {
        TokenBucket bucket = new TokenBucket(5, 1); // 5 capacity, 1 token per second

        for (int i = 0; i < 10; i++) {
            System.out.println("Request " + i + ": " + (bucket.allowRequest() ? "Allowed" : "Blocked"));
            Thread.sleep(500); // simulate time delay
        }
    }
}

