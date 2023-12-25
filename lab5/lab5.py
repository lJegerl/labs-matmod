package org.example;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public class MonteCarloSimulation {

    public static void main(String[] args) {
        double[][] AMatrix =
                {{0.7, -0.3, -0.2},
                {-0.2, 0.2, -0.7},
                {-0.5, 0.1, 2}};
        double[] fVector = {-1, -3, 8};
        double[] actualSolution = {-3.07018, 1.14035, 2.45614};

        Map<Pair<Integer, Integer>, Double> results = new HashMap<>();

        int[] numChainsSet = {10, 30, 60, 100};
        int[] chainLengthSet = {10, 100, 300, 1000};

        for (int numChains : numChainsSet) {
            for (int chainLength : chainLengthSet) {
                double[] computedSolution = solve(AMatrix, fVector, numChains, chainLength);
                System.out.println(numChains + " " + chainLength);
                System.out.println("Computed: " + arrayToString(computedSolution));
                System.out.println("Actual: " + arrayToString(actualSolution) + "\n");

                double error = computeError(computedSolution, actualSolution);
                results.put(new Pair<>(numChains, chainLength), error);
            }
        }
    }

    private static double[] solve(double[][] A, double[] f, int numChains, int chainLength) {
        int n = A.length;
        double[] x = new double[n];

        for (int j = 0; j < n; j++) {
            for (int k = 0; k < numChains; k++) {
                double weight = 1;
                int statePrev = j;
                int stateNew = 0;
                x[j] += f[j];

                Random random = new Random();

                for (int l = 0; l < chainLength; l++) {
                    stateNew = random.nextInt(n);
                    weight *= n * A[statePrev][stateNew];
                    x[j] += weight * f[stateNew];
                    statePrev = stateNew;
                }
            }
            x[j] /= numChains;
        }

        return x;
    }

    private static double computeError(double[] computedSolution, double[] actualSolution) {
        double error = 0;
        for (int i = 0; i < computedSolution.length; i++) {
            error += Math.pow(computedSolution[i] - actualSolution[i], 2);
        }
        return Math.sqrt(error);
    }

    private static String arrayToString(double[] array) {
        StringBuilder sb = new StringBuilder("[");
        for (double value : array) {
            sb.append(value).append(", ");
        }
        sb.delete(sb.length() - 2, sb.length()).append("]");
        return sb.toString();
    }

    static class Pair<K, V> {
        private final K key;
        private final V value;

        public Pair(K key, V value) {
            this.key = key;
            this.value = value;
        }

        public K getKey() {
            return key;
        }

        public V getValue() {
            return value;
        }
    }
}
