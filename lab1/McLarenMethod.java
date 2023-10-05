public class McLarenMethod {
    private MCM generatorD1;
    private MCM generatorD2;
    private int tableSize;
    private long[] table;

    public McLarenMethod(int tableSize) {
        this.tableSize = tableSize;
        this.table = new long[tableSize];
        this.generatorD1 = new MCM(261463909, (long)Math.pow(2,31), 474379977);
        this.generatorD2 = new MCM(234289925, (long)Math.pow(2,31), 3097871);
        initializeTable();
    }

    private void initializeTable() {
        for (int i = 0; i < tableSize; i++) {
            table[i] = generatorD1.generateNext();
        }
    }

    public long generateNext() {
        int s = (int) (generatorD2.generateNext() % tableSize);
        long alpha = table[s];
        long beta = generatorD1.generateNext();
        table[s] = beta;
        return alpha;
    }
}
