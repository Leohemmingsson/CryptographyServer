from database_abstraction import DB
from abe_abstraction import ABE, CPAc17


# x = DB()
# abe = ABE(scheme=CPAc17, attributes=["A", "B"], policy='("A" and "B")')
# abe.load_static_keys_from_sql(x)
# abe.keygen()
# encrypted = abe.encrypt("plaintext")
# decrypted = abe.decrypt(encrypted)

# print(decrypted)


# x.close()


x = DB()
abe = ABE(CPAc17)
pk, msk = abe.generate_static_keys()
pk = str(pk)
msk = str(msk)

x.update_pk_msk(pk, msk, 1)
x.close()
