class Product:
    def __init__(self, id, name, price, rep):
        self.id = id
        self.name = name
        self.price = price
        self.rep = rep

    def __str__(self):
        s = "id=%s, name=%s, price=%s, rep=%s"
        return s % (self.id, self.name, self.price, self.rep)
    def __str__(self):
        s = "id={}, name={}, price={}, rep={}"
        return s.format(self.id, self.name, self.price, self.rep)

if __name__ == "__main__":
    product = Product(1, "Product A", 10.99, "High")
    print(product)

print('-'*40)
from functools import reduce
class Disc:
    def __init__(self, id, name, price, rep):
        self.id = id
        self.name = name
        self.price = price
        self.rep = rep

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_rep(self):
        return self.rep

    def __str__(self):
        return f"id={self.id}, name={self.name}, price={self.price}, rep={self.rep}"

# Creating the list of Disc objects
disc_list = [
    Disc(1, "aa", 100, [1, 2, 3]),
    Disc(2, "bb", 300, [2, 2, 3]),
    Disc(3, "cc", 500, [3, 5, 4]),
    Disc(4, "dd", 600, [4, 4, 4]),
    Disc(5, "ee", 900, [1, 2, 3])
]

# Printing the list of Disc objects
for disc in disc_list:
    print(disc)

# Calculating the sum of prices for discs with price >= 500 and id > 3
filtered_discs = [disc for disc in disc_list if disc.get_price() >= 500 and disc.get_id() > 3]
prices = [disc.get_price() for disc in filtered_discs]
total_sum = reduce(lambda x, y: x + y, prices, 0)

print(f"Sum: {total_sum}")

from functools import reduce
class Disc:
    def __init__(self, id, name, price, rep):
        self.id = id
        self.name = name
        self.price = price
        self.rep = rep

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_rep(self):
        return self.rep

    def __str__(self):
        return f"id={self.id}, name={self.name}, price={self.price}, rep={self.rep}"

# Creating the list of Disc objects
disc_list = [
    Disc(1, "aa", 100, [1, 2, 3]),
    Disc(2, "bb", 300, [2, 2, 3]),
    Disc(3, "cc", 500, [3, 5, 4]),
    Disc(4, "dd", 600, [4, 4, 4]),
    Disc(5, "ee", 900, [1, 2, 3])
]

# Printing the list of Disc objects
for disc in disc_list:
    print(disc)

# Calculating the sum of prices for discs with price >= 500 and id > 3
filtered_discs = [disc for disc in disc_list if disc.get_price() >= 500 and disc.get_id() > 3]
prices = [disc.get_price() for disc in filtered_discs]
total_sum = reduce(lambda x, y: x + y, prices, 0)

print(f"Sum: {total_sum}")


"""
import java.util.List;

public class HWDemo {
    public static void main(String[] args) {
        var list = List.of(
            new Disc(1, "aa", 100, List.of(1, 2, 3)),
            new Disc(2, "bb", 300, List.of(2, 2, 3)),
            new Disc(3, "cc", 500, List.of(3, 5, 4)),
            new Disc(4, "dd", 600, List.of(4, 4, 4)),
            new Disc(5, "ee", 900, List.of(1, 2, 3))
        );
        System.out.println(list);
        var sum = list.stream()
        //    .flatMap(d->d.getRep().stream())
              .peek(System.out::println)
              .filter(d->d.id()>3)
              .map(d->d.price())
            //   .filter(p->p>=500)
        //    .filter(d->d.getID()>3)
        //    .map(d->d.getPrice())
        //    .filter(p->p>-500)
           .reduce(0, (s,e)->s+e);
        System.out.println("Sum: " + sum);
    }
}
record Disc (int id, String name, int price, List<Integer> rep) {}

// class Disc {
//     private int id;
//     private String name;
//     private int price;
//     private List<Integer> rep;

//     public Disc(int id, String name, int price, List<Integer> rep) {
//         this.id = id;
//         this.name = name;
//         this.price = price;
//         this.rep = rep;
//     }

//     public int getID() {
//         return this.id;
//     }

//     public String getName() {
//         return this.name;
//     }

//     public int getPrice() {
//         return this.price;
//     }

//     public List<Integer> getRep() {
//         return this.rep;
//     }

//     @Override
//     public String toString() {
//         var s = "id=%s, name=%s, price=%s, rep=%s";
//         return String.format(s, this.id, this.name, this.price, this.rep);
//     }
// }
"""
