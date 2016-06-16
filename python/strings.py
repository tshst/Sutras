# -*- coding: utf-8 -*-

s = 'hi'
print s[1]  ## i
print len(s) ## 2
print s + ' there' ## hi there

pi = 3.14

text = 'The value of pi is ' + str(pi)
print text


raw = r'aaa and that'
print raw

multi = """It was the best of times.
It was the worst of times. test"""

print multi

st = '    test    '

## Method
print s.lower()
print s.upper()
print raw.strip()
print st.strip()
print s.isalpha()
print s.isdigit()
print s.isspace()
print multi.find('test')

print type(1)
print type(1.1)
print type('日本語')
print u'日本語'.encode('utf-8')
print type(u'日本語'.encode('utf-8'))

### 文字列の操作
#### 連結
print 'Mt' + 'Fuji'
#### 存在チェック
print 'ta' in 'takaoka'
#### 分割
print 'pain-au-chocolat'.split('-')
