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

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        half_len = (m + n + 1) // 2
        imin, imax = 0, m

        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            
            if i < m and nums1[i] < nums2[j - 1]:
                imin = i + 1  # i is too small
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1  # i is too big
            else:  # i is perfect
                if i == 0: max_of_left = nums2[j - 1]
                elif j == 0: max_of_left = nums1[i - 1]
                else: max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left  # Odd case

                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0  # Even case

        raise ValueError("Input arrays are not sorted.")

if __name__ == "__main__":
    solver = Solution()

    nums1 = [1, 3]
    nums2 = [2]
    print("Median is:", solver.findMedianSortedArrays(nums1, nums2))  # Output: 2.0

    nums3 = [1, 2]
    nums4 = [3, 4]
    print("Median is:", solver.findMedianSortedArrays(nums3, nums4))  # Output: 2.5

"""
import java.util.ArrayList;
import java.util.Collections;

public class MedianCalculator {
    public static void main(String[] args) {
        ArrayList<Integer> list1 = new ArrayList<>();
        Collections.addAll(list1, 1, 2, 4, 8, 4);

        ArrayList<Integer> list2 = new ArrayList<>();
        Collections.addAll(list2, 43, 34, 3, 34, 45);

        double median = findMedian(list1, list2);
        System.out.println("中位數是: " + median);
    }

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

}
"""
