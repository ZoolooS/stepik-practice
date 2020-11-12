'''
Программа принимает на вход две строки одинаковой длины,
на первой строке записаны символы исходного алфавита,
на второй строке — символы конечного алфавита,
после чего идёт строка, которую нужно зашифровать переданным ключом,
и ещё одна строка, которую нужно расшифровать.
'''
# ====== imports block ================================== #


# ====== function declaration =========================== #


# ====== main code ====================================== #
orig_alphabet = input()
subst_alphabet = input()
str_for_encript = input()
str_for_decript = input()

alphabet_o2s = {k: v for k, v in zip(orig_alphabet, subst_alphabet)}
alphabet_s2o = {k: v for k, v in zip(subst_alphabet, orig_alphabet)}

print(''.join([alphabet_o2s[el] for el in str_for_encript]))
print(''.join([alphabet_s2o[el] for el in str_for_decript]))

# ====== end of code ==================================== #