print("===Менеджер паролей===")
var_1 = input("Введите ваш новый пароль: ")
fw = open('file/top_secret.txt', 'a', encoding='utf-8')
fw.write(var_1 + '\n')
fw.close()
fr = open('file/top_secret.txt', 'r', encoding='utf-8')
passwords = fr.read()
fr.close()
print("Сохраненные пароли: \n" + passwords)