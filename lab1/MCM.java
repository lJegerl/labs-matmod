 public class MCM {
    private long seed;
    private long multiplier;
    private long modulus;

    public MCM(long seed, long modulus, long c) {
        this.seed = seed;
        this.modulus = modulus;
        this.multiplier = computeMultiplier(c, modulus);
    }

    public long generateNext() {
        seed = (multiplier * seed) % modulus;
        return seed;
    }

    private long computeMultiplier(long c, long modulus) {
        return Math.max(c, modulus - c);
    }
}
