length_ = [[a, b, c] for a in range(1,20) for b in range(1,20) for c in range(1,20)
           if a**2 + b**2 == c**2]
print(length_)

# import java.util.ArrayList;
# import java.util.List;

# public class PythagoreanTriplets {
#     public static void main(String[] args) {
#         List<int[]> triplets = new ArrayList<>();
#         for (int a = 1; a < 20; a++) {
#             for (int b = 1; b < 20; b++) {
#                 for (int c = 1; c < 20; c++) {
#                     if (a*a + b*b == c*c) {
#                         int[] triplet = {a, b, c};
#                         triplets.add(triplet);
#                     }
#                 }
#             }
#         }
#         System.out.println(triplets);
#     }
# }
