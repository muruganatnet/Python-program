#Big string
str1='''Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale. Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation'''

#Code to get each word in a List
str1=str1.replace(',','')
dic_cnt=dict()
for word in str1.split(' '):
   if word in dic_cnt:
       dic_cnt[word]+=1
   else: 
       dic_cnt[word]=1

#Sort them with the Dic Value first
word_cnt=sorted(((v,k) for k,v in dic_cnt.items()),reverse=True)  

#Pick first five top words
for i in range(5):
   print(word_cnt[i]) 
    
    
