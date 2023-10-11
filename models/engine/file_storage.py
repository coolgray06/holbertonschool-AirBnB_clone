for id, dictionary in object_dict.items():
    class_name = dictionary['__class__']
    final_dict[id] = self.classes()[class_name](**dictionary)
FileStorage.__objects = final_dict