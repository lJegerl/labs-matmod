public class Main {
    public static void main(String[] args) {
        int size = 1000;
        McLarenMethod generator1 = new McLarenMethod(size);
        MCM generator2 = new MCM(261463909, (long)Math.pow(2,31), 474379977);
        long mcmValue = 0;
        long mcLarenValue = 0;
        for (int i = 0; i < size; i++) {
            mcmValue = generator1.generateNext();
            mcLarenValue = generator2.generateNext();
        }
        System.out.println("McLaren " + (1000) + " times: " + mcmValue);
        System.out.println("MCM " + (1000) + " times: " + mcLarenValue);
    }
}