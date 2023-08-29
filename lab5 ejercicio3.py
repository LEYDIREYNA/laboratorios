nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
nums3 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#a
conj1 = set(nums1)
conj2 = set(nums2)
conj3 = set(nums3)
#b
conjunto_comun = conj1.intersection(conj2, conj3)
print(conjunto_comun)
#c
conjunto_simetria = conj1.symmetric_difference(conj2)
conjunto_sim = conjunto_simetria.symmetric_difference(conj3)
print(conjunto_sim)
#d
conj_dif = conj1.difference(conj3)
print(conj_dif)
#e
tupla_comun =tuple(conjunto_comun)
tupla_sim =tuple(conjunto_sim)
tupla_dif =tuple(conj_dif)
sum_prim_ult_comun =tupla_comun[0] + tupla_comun[-1]
sum_prim_ult_sim =tupla_sim[0] + tupla_sim[-1]
sum_prim_ult_dif = tupla_dif[0] + tupla_dif[-1]
print(sum_prim_ult_comun)
print(sum_prim_ult_sim)
print(sum_prim_ult_dif)