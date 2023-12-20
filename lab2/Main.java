import java.util.Random;

public class Main {
    public static void main(String[] args) {
        int n = 1000;

        double pBernoulli = 0.7;
        double lambdaPoisson = 0.5;
        double pGeometric = 0.1;
        int rInverseBinomial = 4;
        double pInverseBinomial = 0.2;

        Random random = new Random();

        int[] bernoulliSamples = new int[n];
        for (int i = 0; i < n; i++) {
            bernoulliSamples[i] = random.nextDouble() < pBernoulli ? 1 : 0;
        }
        double meanBernoulli = calculateMean(bernoulliSamples);
        double varianceBernoulli = calculateVariance(bernoulliSamples);

        int[] poissonSamples = new int[n];
        for (int i = 0; i < n; i++) {
            poissonSamples[i] = generatePoisson(lambdaPoisson, random);
        }
        double meanPoisson = calculateMean(poissonSamples);
        double variancePoisson = calculateVariance(poissonSamples);

        int[] geometricSamples = new int[n];
        for (int i = 0; i < n; i++) {
            geometricSamples[i] = generateGeometric(pGeometric, random);
        }
        double meanGeometric = calculateMean(geometricSamples);
        double varianceGeometric = calculateVariance(geometricSamples);

        int[] inverseBinomialSamples = new int[n];
        for (int i = 0; i < n; i++) {
            inverseBinomialSamples[i] = generateInverseBinomial(rInverseBinomial, pInverseBinomial, random);
        }
        double meanInverseBinomial = calculateMean(inverseBinomialSamples);
        double varianceInverseBinomial = calculateVariance(inverseBinomialSamples);


        System.out.println("Бернулли (Bi(1, 0.7)):");
        System.out.println("Истинное математическое ожидание: " + pBernoulli);
        System.out.println("Оценка математического ожидания: " + meanBernoulli);
        System.out.println("Истинная дисперсия: " + (pBernoulli * (1 - pBernoulli)));
        System.out.println("Оценка дисперсии: " + varianceBernoulli);
        System.out.println();

        System.out.println("Пуассон (P(0.5)):");
        System.out.println("Истинное математическое ожидание: " + lambdaPoisson);
        System.out.println("Оценка математического ожидания: " + meanPoisson);
        System.out.println("Истинная дисперсия: " + lambdaPoisson);
        System.out.println("Оценка дисперсии: " + variancePoisson);
        System.out.println();

        System.out.println("Геометрическое (G(0.1)):");
        System.out.println("Истинное математическое ожидание: " + (1 / pGeometric));
        System.out.println("Оценка математического ожидания: " + meanGeometric);
        System.out.println("Истинная дисперсия: " + ((1 - pGeometric) / (pGeometric * pGeometric)));
        System.out.println("Оценка дисперсии: " + varianceGeometric);
        System.out.println();

        System.out.println("Обратное биномиальное (Bi(4, 0.2)):");
        System.out.println("Истинное математическое ожидание: " + (rInverseBinomial / pInverseBinomial));
        System.out.println("Оценка математического ожидания: " + meanInverseBinomial);
        System.out.println("Истинная дисперсия: " + (rInverseBinomial * (1 - pInverseBinomial) / (pInverseBinomial * pInverseBinomial)));
        System.out.println("Оценка дисперсии: " + varianceInverseBinomial);

    }


    public static double calculateMean(int[] samples) {
        double sum = 0;
        for (int sample : samples) {
            sum += sample;
        }
        return sum / samples.length;
    }


    public static double calculateVariance(int[] samples) {
        double mean = calculateMean(samples);
        double sumSquaredDiff = 0;
        for (int sample : samples) {
            sumSquaredDiff += Math.pow(sample - mean, 2);
        }
        return sumSquaredDiff / (samples.length - 1);
    }


    public static int generatePoisson(double lambda, Random random) {
        double L = Math.exp(-lambda);
        double p = 1.0;
        int k = 0;
        do {
            k++;
            p *= random.nextDouble();
        } while (p > L);
        return k - 1;
    }


    public static int generateGeometric(double p, Random random) {
        return (int) (Math.log(1.0 - random.nextDouble()) / Math.log(1.0 - p));
    }


    public static int generateInverseBinomial(int r, double p, Random random) {
        int successes = 0;
        int trials = 0;
        while (successes < r) {
            if (random.nextDouble() < p) {
                successes++;
            }
            trials++;
        }
        return trials;
    }
}
