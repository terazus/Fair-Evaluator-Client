import requests
import json

mapping = {
    "@id": "id",
    "@context": "context",
    "@type": "type",
    "http://purl.org/dc/elements/1.1/authoredBy": "author",
    "http://purl.org/dc/elements/1.1/license": "license",
    "http://purl.org/dc/elements/1.1/title": "title",
    "http://purl.org/dc/elements/1.1/creator": "creator",
    "http://purl.org/pav/version": "version",
    "http://rdfs.org/ns/void#description": "description",
    "http://www.w3.org/ns/dcat#entities": "entities",
    "http://www.w3.org/ns/dcat#contactPoint": "contact",
    "http://www.w3.org/ns/dcat#identifier": "identifier",
    "http://www.w3.org/ns/dcat#publisher": "publisher",
    "http://www.w3.org/ns/ldp#contains": "metrics",
}
baseURL = "https://w3id.org/FAIR_Evaluator"
headers = {
    "Accept-Type": "application/json"
}
not_found = {"message": "¨Problem with the server, try again!"}


class Collection:

    def __init__(self, **kwargs):

        if 'collection' in kwargs.keys():
            data = kwargs['collection']

            for attribute in mapping:
                if attribute in data.keys():
                    value = data[attribute]
                    if type(value) is str:
                        value = value.replace("\n", " ").replace("\r", " ").replace('"', "'")
                        exec('self.%s = "%s"'
                             % (mapping[attribute], value)
                             )
                    else:
                        exec('self.%s = %s'
                             % (mapping[attribute], value)
                             )

        else:
            print('Attempt to create new collection')

    def get_properties(self):
        return list(vars(self).keys())

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)

    def refresh(self):
        identifier = self.id.split('/')[-1]
        url = baseURL + "/collections/" + identifier + ".json"
        request = requests.get(url, headers=headers, verify=False)
        if request.status_code is not "404":
            collection = json.loads(request.text)
            for attribute in mapping:
                if attribute in collection.keys():
                    value = collection[attribute]
                    if type(value) is str:
                        value = value.replace("\n", " ").replace("\r", " ").replace('"', "'")
                        exec('self.%s = "%s"' % (mapping[attribute], value))
                    else:
                        exec('self.%s = %s' % (mapping[attribute], value))
        else:
            return not_found

    def get_metrics(self):
        for metricID in self.metrics:
            metric = Metric(identifier=metricID)
        pass

    def evaluate(self, resource=None, author=None, title=None):
        pass


class Metric:

    def __init__(self, **kwargs):
        if 'identifier' in kwargs.keys():
            self.metric_id = kwargs['identifier'].split('/')[-1]
            data = self.refresh_metric()

            if 'message' not in data.keys():
                for field in data:
                    print(field)

    def refresh_metric(self):
        url = baseURL + "/metrics/" + self.metric_id + ".json"
        request = requests.get(url, headers=headers, verify=False)
        if request.status_code is not "404" and request.status_code is not 404:
            return json.loads(request.text)
        else:
            return not_found
