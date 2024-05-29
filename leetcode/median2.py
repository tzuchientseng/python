"""
import java.util.ArrayList;
import java.util.Collections;

public class MedianCalculator {

    public static double findMedian(ArrayList<Integer> list1, ArrayList<Integer> list2) {
        ArrayList<Integer> combinedList = new ArrayList<>(list1);
        combinedList.addAll(list2);
        Collections.sort(combinedList);

        int size = combinedList.size();
        if (size % 2 == 1) {
            return combinedList.get(size / 2);
        } else {
            return (combinedList.get(size / 2 - 1) + combinedList.get(size / 2)) / 2.0;
        }
    }

    public static void main(String[] args) {
        ArrayList<Integer> list1 = new ArrayList<>();
        Collections.addAll(list1, 1, 2, 4, 8, 4);

        ArrayList<Integer> list2 = new ArrayList<>();
        Collections.addAll(list2, 43, 34, 3, 34, 45);

        double median = findMedian(list1, list2);
        System.out.println("中位數是: " + median);
    }
}
"""

def Medain(a, b):
    sum_list = a + b
    sum_list.sort()
    if len(sum_list) % 2 == 1:
        return sum_list[(len(sum_list) // 2)] 
    else: 
        mid = len(sum_list) // 2
        return (sum_list[mid - 1] + sum_list[mid]) / 2 
list_1 = [1, 2, 4, 8, 4]
list_2 = [43, 34, 3, 34, 45]
print(Medain(list_1, list_2))