from fairCollections import Collections

'''
class Evaluator:

    def __init__(self):
        self.__baseURL = "https://w3id.org/FAIR_Evaluator"
        self.__header = {
            "Accept-Type": "application/json"
        }

        # COLLECTIONS
        self.__collections = None
        self.__collections_detailed = {}

        # METRICS
        self.__metrics = None
        self.__metrics_detailed = {}

        # EVALUATIONS
        self.__evaluations = None
        self.__evaluations_detailed = {}

    """ ******************************************************************************************
                                                METRICS 
    ****************************************************************************************** """

    def update_metrics(self):
        """ Updates the list of available metrics
        """
        url = self.__baseURL + "/metrics.json"
        request = requests.get(url, headers=self.__header, verify=False)
        self.__metrics = json.loads(request.text)

    def metrics(self):
        """ Loads the list of metrics if not loaded and return them

        :return: (dict) the list of metrics
        """
        if self.__metrics is None:
            self.update_metrics()
        return self.__metrics

    def update_metric(self, identifier):
        """ Updates the metric which has the given identifier

        :param identifier: int
        """
        url = self.__baseURL + "/metrics/" + str(identifier) + ".json"
        request = requests.get(url, headers=self.__header, verify=False)
        self.__metrics_detailed[identifier] = json.loads(request.text)

    def metric(self, identifier):
        """ Return the metric for the given identifier

        :param identifier: int
        :return: (dict) a metric
        """
        if identifier not in self.__metrics_detailed.keys():
            self.update_metric(identifier)
        return self.__metrics_detailed[identifier]

    """ ******************************************************************************************
                                                EVALUATIONS 
    ****************************************************************************************** """

    def update_evaluations(self):
        """ Updates the list of evaluations metrics
        """
        url = self.__baseURL + "/evaluations.json"
        request = requests.get(url, headers=self.__header, verify=False)
        self.__evaluations = json.loads(request.text)

    def evaluations(self):
        """ Loads the list of evaluations if not loaded and return them

        :return: (dict) the list of evaluations
        """
        if self.__evaluations is None:
            self.update_evaluations()
        return self.__evaluations

    def update_evaluation(self, identifier):
        """ Updates the evaluation which has the given identifier

        :param identifier: int
        """
        url = self.__baseURL + "/evaluations/" + str(identifier) + "/result.json"
        request = requests.get(url, headers=self.__header, verify=False)
        if request.status_code == "404":
            return {
                "message": "Couldn't find Evaluation with '" + str(identifier) + "'=4"
            }
        self.__evaluations_detailed[identifier] = json.loads(request.text)

    def evaluation(self, identifier):
        """ Return the evaluation for the given identifier

        :param identifier: int
        :return: (dict) an evaluation
        """
        if identifier not in self.__evaluations_detailed.keys():
            self.update_evaluation(identifier)
        return self.__evaluations_detailed[identifier]
'''

if __name__ == '__main__':
    collections = Collections()
    collections.get_collection(4).get_metrics()
