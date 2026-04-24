In Byteland,people don't use standard e-mail services like gmail,yahoo-mail etc.Instead they have their own e-mail service know as Bytemail.In Bytemail, encryption of e-mails is done using a special algorithm known as Bytecryption algorithm.It works as follows:
 1)All the text is converted into lower-case alphabets only('a'-'z') using some algorithm Q .
 2)Now , for each string str(say) in the text,the Bytecryption algorithms encrypts the string as follows:
        Start with the given string str and an empty string k. The algorithm runs in multiple steps.For each step,str and k are modified as follows:
           a) If the length of str is odd, the middle character of s is added to the end of k, and then deleted from str.
            b)If the length of str is even, the two characters in the middle of str are compared. The smaller one of them (either one in case of a tie) is added to the end of k, and then deleted from str.
        If after some step the string str is empty, the algorithm terminates. The output of the algorithm is the final string t.

Now your job is to encrypt  a string str and output it.

Input
The first line of input contains T,the number of test cases.The next T lines contain a string str which you need to encrypt.

Output
Output T lines each corresponding to the encrypted string.

Constraints
1)Size of the string str ≤ 50 and ≥1
2)Each character in str is a lowercase letter('a'-'z').

SAMPLE INPUT
2
aaaaaaaa
adappadsdsdas

SAMPLE OUTPUT
aaaaaaaa
dasdppsadadas
