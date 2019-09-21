#big string
str1='''Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale. Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation'''

#code to do next words for each words in dictionary dic_cnt
str1=str1.replace(',','')
dic_cnt=dict()
lis_word=str1.split(' ')
i=0
for word in lis_word:
   i+=1
   if word in dic_cnt:
       next_word=''
       l1=dic_cnt[word]
       try:
           next_word=lis_word[i]
           if next_word not in l1:
               l1.append(next_word)
       except IndexError:
           None
   else:
       l2=[]
       next_word=''
       try:
           next_word=lis_word[i]
       except IndexError:
           None
       l2.append(next_word)
       dic_cnt[word]=l2
       
       
       
print(dic_cnt)
        