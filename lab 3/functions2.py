# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def imdb(arr):
    string = input('type a film name:\n')
    j = len(arr)
    for i in range(len(arr)):
        if arr[i]["name"] == string:
            j = i
            break
    if j == len(arr):
        print("There is no film with this name")
        return False
    if arr[j]['imdb'] > 5.5:
        return True
    return False
print(imdb(movies))

#2
def sublis(arr):
    lis = []
    for i in range(len(arr)):
        if arr[i]["imdb"] > 5.5:
            lis.append(arr[i]["name"])
    return lis
print(sublis(movies))

#3
def categ(arr):
    string = input('type a film category name:\n')
    lis = []
    for i in range(len(arr)):
        if arr[i]["category"] == string:
            lis.append(arr[i]["name"])
    if len(lis) == 0:
        print("No films from this category")
    return lis
print(categ(movies))

#4
def average(arr):
    n = int(input('type number of films:\n'))
    lis =[]
    for i in range(n):
        string=input("name of film number " + str(i+1) + ": ")
        lis.append(string)
    count = 0.0
    for i in lis:
        for j in range(len(arr)):
            if arr[j]['name'] == i:
                count += arr[j]["imdb"]
                break
    return count/len(lis)
print("average imdb score is: " + str(average(movies)))

#5
def imdb_avg(arr):
    string = input("write a category\n")
    count = 0
    number = 0
    for i in range(len(arr)):
        if arr[i]['category'] == string:
            count += arr[i]['imdb']
            number += 1
    return count/number
print('average imdb score for your category is: ' + str(imdb_avg(movies)))