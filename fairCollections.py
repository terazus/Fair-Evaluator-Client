import requests
import json
from baseTypes import (
    Collection,
    not_found,
    baseURL,
    headers,
)


class Collections:

    class __Collections:

        def __init__(self):
            self.__all = None
            self.get_all()

        def get_all(self):
            url = baseURL + "/collections.json"
            request = requests.get(url, headers=headers, verify=False)
            if self.__all is None:
                self.__all = {}
                if request.status_code is not "404":
                    for item in json.loads(request.text):
                        collection = Collection(collection=item)
                        identifier = collection.id
                        self.__all[identifier.split('/')[-1]] = collection
                    return self.__all
                else:
                    return not_found
            else:
                return self.__all

    instance = None

    def __init__(self):
        if not Collections.instance:
            Collections.instance = Collections.__Collections()
        else:
            pass

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __str__(self):
        return json.dumps(self.__serialize(), indent=4)

    def __serialize(self):
        serialized_collections = {}
        for collectionID in self.__all:
            serialized_collections[collectionID] = self.__all[collectionID].__dict__
        return serialized_collections

    def get_collection(self, identifier):
        if str(identifier) not in self.__all.keys():
            return not_found
        return self.__all[str(identifier)]
