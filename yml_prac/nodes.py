import yaml
import os

class Node:
    def __init__(self,**kwargs):
        self.kwargs=kwargs


    def __repr__(self):
        return ','.join(["{}={}".format(x,y) for x,y in self.kwargs.items()])

class YAML:
    def __init__(self,filename=None):
        self.__filenane=filename
        self.__config_path=os.path.join(os.curdir,self.__filenane)
        self.__config=self.__load_config()
    def __load_config(self):
        try:
           with open (self.__config_path) as f:
               config = yaml.safe_load(f)
        except Exception as e:
            raise e
        return config
    def get_config(self,name):
        return self.__config[name]

    def get_all_data(self):
        return self.__config


def main(service_file,nodes_file,service_name):
    service_config=YAML(service_file)
    nodes_config=YAML(nodes_file)
    nodes=service_config.get_config(service_name)
    for node in nodes:
        config=nodes_config.get_config(node)
        nodeobj=Node(**config)
        print(nodeobj)







if __name__ == '__main__':
    main("services","nodes","servicea")