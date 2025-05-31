def remove_spaces(input_string):
    # return input_string.replace(" ", "")
    return input_string.replace("，", " ")

old_text = (
"""

"""
)

cleaned_text = remove_spaces(old_text)
print(cleaned_text)

"""
public class RemoveSpaces {

    public static String removeSpaces(String input) {
        return input.replace(" ", "");
    }

    public static void main(String[] args) {
        String oldText = "your text here";

        String cleanedText = removeSpaces(oldText);
        System.out.println(cleanedText);
    }
}
"""
