package concurrency;

import java.lang.ScopedValue;

public class ScopedValueDemo {
    static final ScopedValue<String> USER = ScopedValue.newInstance();

    public static void main(String[] args) throws Exception {
        // Run the scoped logic directly inside the virtual thread
        Thread vt = Thread.ofVirtual().unstarted(() -> {
            ScopedValue.where(USER, "Sudhir").run(() -> {
                System.out.println("Hello, " + USER.get());
            });
        });

        vt.start();
        vt.join();
    }
}
