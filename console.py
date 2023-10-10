from models import base_model as bm



model_1 = bm.base_model("My Name")

model_2 = bm.base_model.save(model_1)

model_3 = bm.base_model.update_name (model_2, "Dee")

print(model_1,model_2)








person2 = bm.user.createUser("pas!","Eli",26)


print(person1)
print(person2)