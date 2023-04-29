import wolframalpha
import wikipedia
while True:
    inp = input("Question: ")
    try:
        app_id = "PGQYQT-J7E5Y94U3K"
        client = wolframalpha.Client(app_id)
        res = client.query(inp)
        ans = next(res.results).text
        print(ans)
    except:
        print (wikipedia.summary(inp))