"""Restaurant rating lister."""


# put your code here

dictionary = {}
def main():
        
    with open('scores.txt') as f:
        lines = f.readlines()
        print(lines)
        for line in lines:
            restaurant, score = line.split(":")
            dictionary[restaurant] = int(score)
    rest_name = str(input('Enter the restaurant\'s name:\n'))
    rest_rate = int(input('Enter the restaurant\'s rating:\n'))
    dictionary[rest_name] = rest_rate

def sort(dictionary):
    sorted_keys = dictionary.items()
    new_values = sorted(sorted_keys)
    print(new_values)

main()
sort(dictionary)