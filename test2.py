# from langchain.agents import create_agent


# def weather_agent(city:str) -> str:
#     return f"the whether in {city} is sunny"


# agent = create_agent(
#     tools=[weather_agent],
#     model="gpt-3.5-turbo",
#     system_prompt="you are a helpful assistant"
# )

# response = agent.invoke(
#     {"messages": [{"role": "user", "content": "what is the weather in New York?"}]}
# )

# print(response)






















#Q1. Reverse a string without using built-in reverse

# a="sachin awati"
# # b=a[::-1]
# # # print(b)

# # b=reversed(a)
# # print(''.join(b))


# b=a.split()[::-1]

# print(' '.join(b))




# def reverse_string(s):
#     result = ""
#     for ch in s:
#         result = ch + result
#     return result

# print(reverse_string("Sachin"))







# # is prime

# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# print(is_prime(12))



# # is palindrome sequence
# def is_palindrome(s):
#     if s == s[::-1]:
#         return True
#     else:
#         return False
    
# print(is_palindrome("madam"))





#Remove duplicates from a list
#a=[1,23,4,5,2,55,33,54,55,1,23,4,5,45,232,111]
# b=set(a)
# print(b)


# def remove_duplicates_order(lst):
#     seen = set()
#     result = []
#     for x in lst:
#         if x not in seen:
#             seen.add(x)
#             result.append(x)
#     return result
# a=[1,23,4,5,2,55,33,54,55,1,23,4,5,45,232,111]
# print(remove_duplicates_order(a))


# # Count word frequency
# def word_ferquency(text):
#     freq={}

#     for word in text.split():
#         freq[word]=freq.get(word,0)+1
#     return freq

# print(word_ferquency("this is a test this is only a test"))







# from langchain.agents import create_agent

# def weather_agent(city:str) -> str:
#     return f"the weather in {city} is sunny"

# agent=create_agent(
#     tools=[weather_agent],
#     model="gpt-3.5-turbo",
#     system_prompt="you are a helpful assistant"
# )


# agent.invoke(
#     {"messages":[{"role":"user", "content":"what is the weather in newyork?"}]}
# )


from fastapi import FastAPI

app=FastAPI()

@app.get("/predict")
def predict(x:int):
    return {"result": x**2}

print("server started")



